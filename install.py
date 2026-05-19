#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Dev Workflows Installer
Run with: uv run install.py [--uninstall] [--dry-run]
"""

import argparse
import json
import os
import shutil
import sys
import urllib.request
from pathlib import Path
from datetime import datetime

# ─── Config ───────────────────────────────────────────────────────────────────

REPO = "fnhernandorena/agents_prompts"
BRANCH = "main"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"

SKILLS = [
    ("workflow-init",     "Bootstrap a new multi-repo workspace"),
    ("workflow-continue", "Resume an existing workspace session"),
    ("workflow-add-repo", "Add a new repo to an existing workspace"),
    ("project-init",      "Bootstrap a new single-repo project"),
    ("project-continue",  "Start a session on an existing project"),
    ("project-handoff",   "Close a session cleanly for the next agent"),
    ("project-audit",     "Assess a project with no or stale documentation"),
    ("task-plan",         "Produce a detailed implementation plan"),
    ("task-do",           "Execute a planned task step by step"),
    ("task-review",       "Pre-PR code review (correctness, security, tests)"),
    ("task-hotfix",       "Urgent production fix with controlled speed"),
]

SKILL_NAMES = [s[0] for s in SKILLS]

TOOLS = [
    {
        "id": "claude",
        "name": "Claude Code",
        "binaries": ["claude"],
        "detect": [Path.home() / ".claude"],
        "global_dir": Path.home() / ".claude" / "skills",
        "project_subdir": Path(".claude") / "skills",
        "files_per_skill": ["SKILL.md", "prompt.md"],
        "global_label": "~/.claude/skills/",
        "project_label": ".claude/skills/",
    },
    {
        "id": "codex",
        "name": "Codex (OpenAI)",
        "binaries": ["codex"],
        "detect": [Path.home() / ".codex", Path.home() / ".agents"],
        "global_dir": Path.home() / ".agents" / "skills",
        "project_subdir": Path(".agents") / "skills",
        "files_per_skill": ["SKILL.md", "prompt.md"],
        "global_label": "~/.agents/skills/",
        "project_label": ".agents/skills/",
    },
    {
        "id": "cursor",
        "name": "Cursor",
        "binaries": ["cursor"],
        "detect": [Path.home() / ".cursor"],
        "global_dir": Path.home() / ".cursor" / "skills",
        "project_subdir": Path(".cursor") / "skills",
        "files_per_skill": ["SKILL.md", "prompt.md"],
        "global_label": "~/.cursor/skills/",
        "project_label": ".cursor/skills/",
    },
    {
        "id": "gemini",
        "name": "Gemini CLI",
        "binaries": ["gemini"],
        "detect": [Path.home() / ".gemini"],
        "global_dir": Path.home() / ".gemini",
        "project_subdir": Path("."),
        "files_per_skill": None,
        "context_file": "GEMINI.md",
        "global_label": "~/.gemini/GEMINI.md",
        "project_label": "./GEMINI.md",
    },
    {
        "id": "opencode",
        "name": "OpenCode",
        "binaries": ["opencode"],
        "detect": [
            Path.home() / ".config" / "opencode",
            Path.home() / ".opencode",
        ],
        "global_dir": Path.home() / ".config" / "opencode",
        "project_subdir": Path("."),
        "files_per_skill": None,
        "context_file": "AGENTS.md",
        "global_label": "~/.config/opencode/AGENTS.md",
        "project_label": "./AGENTS.md",
    },
]

# ─── ANSI colors ──────────────────────────────────────────────────────────────

USE_COLOR = sys.stdout.isatty() and os.name != "nt"

def c(text, code):
    return f"\033[{code}m{text}\033[0m" if USE_COLOR else text

def bold(t):  return c(t, "1")
def green(t): return c(t, "32")
def yellow(t):return c(t, "33")
def red(t):   return c(t, "31")
def cyan(t):  return c(t, "36")
def dim(t):   return c(t, "2")

# ─── Source detection ─────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent.resolve()
LOCAL_SKILLS = SCRIPT_DIR / "skills"
SOURCE = "local" if LOCAL_SKILLS.exists() else "remote"

def get_skill_files(skill: str) -> dict[str, str]:
    """Return {filename: content} for a skill, from local or remote."""
    if SOURCE == "local":
        result = {}
        for fname in ["SKILL.md", "prompt.md"]:
            path = LOCAL_SKILLS / skill / fname
            if path.exists():
                result[fname] = path.read_text(encoding="utf-8")
        return result
    else:
        result = {}
        for fname in ["SKILL.md", "prompt.md"]:
            url = f"{RAW_BASE}/skills/{skill}/{fname}"
            try:
                with urllib.request.urlopen(url, timeout=10) as r:
                    result[fname] = r.read().decode("utf-8")
            except Exception as e:
                raise RuntimeError(f"Failed to fetch {url}: {e}") from e
        return result

def get_context_file(name: str) -> str:
    """Fetch a root context file (CLAUDE.md, GEMINI.md, AGENTS.md)."""
    if SOURCE == "local":
        # AGENTS.md is a symlink to CLAUDE.md
        src = "CLAUDE.md" if name == "AGENTS.md" else name
        path = SCRIPT_DIR / src
        if path.exists():
            return path.read_text(encoding="utf-8")
        raise FileNotFoundError(f"Missing {src}")
    else:
        src = "CLAUDE.md" if name == "AGENTS.md" else name
        url = f"{RAW_BASE}/{src}"
        try:
            with urllib.request.urlopen(url, timeout=10) as r:
                return r.read().decode("utf-8")
        except Exception as e:
            raise RuntimeError(f"Failed to fetch {url}: {e}") from e

# ─── Interactive menus ────────────────────────────────────────────────────────

def detect_tool(tool: dict) -> bool:
    for path in tool["detect"]:
        if path.exists():
            return True
    for binary in tool.get("binaries", []):
        if shutil.which(binary):
            return True
    return False

def _getch() -> str:
    """Read one keypress. Returns 'up', 'down', 'enter', 'space', or the char."""
    if os.name == "nt":
        import msvcrt
        ch = msvcrt.getch()
        if ch in (b"\x00", b"\xe0"):
            ch2 = msvcrt.getch()
            if ch2 == b"H": return "up"
            if ch2 == b"P": return "down"
            return ""
        if ch == b"\r":   return "enter"
        if ch == b" ":    return "space"
        if ch == b"\x03": raise KeyboardInterrupt
        try: return ch.decode("utf-8").lower()
        except: return ""
    else:
        import termios, tty, select
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = os.read(fd, 1)
            if ch == b"\x1b":
                # read rest of escape sequence in one shot
                if select.select([fd], [], [], 0.1)[0]:
                    rest = os.read(fd, 6)
                    seq = ch + rest
                    if seq[:3] == b"\x1b[A": return "up"
                    if seq[:3] == b"\x1b[B": return "down"
                return "esc"
            if ch in (b"\r", b"\n"): return "enter"
            if ch == b" ":           return "space"
            if ch == b"\x03":        raise KeyboardInterrupt
            if ch == b"\x04":        raise EOFError
            try: return ch.decode("utf-8").lower()
            except: return ""
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


def _clear_lines(n: int):
    if n > 0 and USE_COLOR:
        sys.stdout.write(f"\033[{n}A\033[J")
        sys.stdout.flush()


def checkbox_menu(title: str, items: list[tuple[str, str]], pre_selected: set[int]) -> set[int]:
    """Arrow-key + space checkbox. Returns selected indices."""
    selected = set(pre_selected)
    cursor = 0
    n = len(items)
    lines_drawn = 0
    while True:
        _clear_lines(lines_drawn)
        out = [f"\n  {bold(title)}"]
        for i, (name, desc) in enumerate(items):
            ptr   = "▶" if i == cursor else " "
            check = green("✓") if i in selected else dim("·")
            nfmt  = bold(name) if i == cursor else name
            out.append(f"  {ptr} [{check}] {nfmt:<28} {dim(desc)}")
        out.append(f"\n  {dim('↑↓ move   space toggle   a all   n none   enter confirm')}")
        block = "\n".join(out)
        print(block)
        lines_drawn = block.count("\n") + 1
        try:
            key = _getch()
        except (KeyboardInterrupt, EOFError):
            print(); sys.exit(0)
        if   key == "up":    cursor = (cursor - 1) % n
        elif key == "down":  cursor = (cursor + 1) % n
        elif key == "space": selected ^= {cursor}
        elif key == "a":     selected = set(range(n))
        elif key == "n":     selected = set()
        elif key in ("enter", "d"): return selected
        elif key in ("q", "esc"):   print(); sys.exit(0)


def radio_menu(title: str, options: list[str], descriptions: list[str] | None = None) -> int:
    """Arrow-key radio menu. Returns selected index."""
    cursor = 0
    n = len(options)
    descs = descriptions or [""] * n
    lines_drawn = 0
    while True:
        _clear_lines(lines_drawn)
        out = [f"\n  {bold(title)}"]
        for i, (opt, desc) in enumerate(zip(options, descs)):
            ptr  = "▶" if i == cursor else " "
            ofmt = bold(opt) if i == cursor else opt
            out.append(f"  {ptr}  {ofmt:<22} {dim(desc)}")
        out.append(f"\n  {dim('↑↓ move   enter select')}")
        block = "\n".join(out)
        print(block)
        lines_drawn = block.count("\n") + 1
        try:
            key = _getch()
        except (KeyboardInterrupt, EOFError):
            print(); sys.exit(0)
        if   key == "up":   cursor = (cursor - 1) % n
        elif key == "down": cursor = (cursor + 1) % n
        elif key == "enter": return cursor
        elif key in ("q", "esc"): print(); sys.exit(0)


def confirm(prompt: str, default: bool = True) -> bool:
    hint = f"{bold('Y')}/n" if default else f"y/{bold('N')}"
    sys.stdout.write(f"\n  {prompt} [{hint}] ")
    sys.stdout.flush()
    try:
        key = _getch()
    except (KeyboardInterrupt, EOFError):
        print(); sys.exit(0)
    print()
    if key == "enter":
        return default
    return key == "y" if not default else key != "n"

# ─── Installation logic ───────────────────────────────────────────────────────

def backup_path(p: Path) -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return p.with_suffix(f".bak_{ts}")

def write_file(dest: Path, content: str, dry: bool) -> str:
    """Write file, backup if exists. Returns status label."""
    if dest.exists():
        if dry:
            return yellow("update")
        shutil.copy2(dest, backup_path(dest))
        dest.write_text(content, encoding="utf-8")
        return yellow("updated")
    else:
        if dry:
            return green("new")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")
        return green("created")

def install_skill(skill: str, dest_dir: Path, dry: bool) -> list[str]:
    """Install SKILL.md + prompt.md into dest_dir/skill/. Returns log lines."""
    log = []
    try:
        files = get_skill_files(skill)
    except Exception as e:
        return [f"  {red('ERROR')} {skill}: {e}"]
    for fname, content in files.items():
        dest = dest_dir / skill / fname
        status = write_file(dest, content, dry)
        log.append(f"  {status}  {dim(str(dest))}")
    return log

def install_context_file(name: str, dest_dir: Path, dry: bool) -> list[str]:
    try:
        content = get_context_file(name)
    except Exception as e:
        return [f"  {red('ERROR')} {name}: {e}"]
    dest = dest_dir / name
    status = write_file(dest, content, dry)
    return [f"  {status}  {dim(str(dest))}"]

def uninstall_skill(skill: str, dest_dir: Path, dry: bool) -> list[str]:
    skill_dir = dest_dir / skill
    if not skill_dir.exists():
        return [f"  {dim('skip')}   {dim(str(skill_dir))} (not found)"]
    if dry:
        return [f"  {red('remove')} {dim(str(skill_dir))}"]
    shutil.rmtree(skill_dir)
    return [f"  {red('removed')} {dim(str(skill_dir))}"]

# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Dev Workflows installer")
    parser.add_argument("--uninstall", action="store_true", help="Remove installed skills")
    parser.add_argument("--dry-run",   action="store_true", help="Preview changes, write nothing")
    args = parser.parse_args()

    print()
    print(bold("  ╔══════════════════════════════════════╗"))
    print(bold("  ║       Dev Workflows Installer        ║"))
    print(bold("  ╚══════════════════════════════════════╝"))
    print(f"  Source: {cyan(SOURCE)}  |  Mode: {cyan('uninstall' if args.uninstall else 'install')}  |  Dry-run: {cyan(str(args.dry_run))}")

    if SOURCE == "remote":
        print(f"\n  {yellow('!')} Local skills/ not found. Files will be downloaded from GitHub.")
        print(f"  Repo: {dim(REPO)}")
        if not confirm("Continue with remote download?"):
            sys.exit(0)

    # ── Step 1: Select tools ─────────────────────────────────────────────────
    tool_items = [(t["name"], green("detected") if detect_tool(t) else dim("not detected")) for t in TOOLS]
    pre_sel = {i for i, t in enumerate(TOOLS) if detect_tool(t)}
    sel_tools = checkbox_menu("Select tools to install for:", tool_items, pre_sel)

    if not sel_tools:
        print(red("\n  No tools selected. Exiting."))
        sys.exit(0)

    selected_tools = [TOOLS[i] for i in sorted(sel_tools)]

    # ── Step 2: Scope ────────────────────────────────────────────────────────
    global_paths  = "  ·  ".join(t.get("global_label",  "") for t in selected_tools)
    project_paths = "  ·  ".join(t.get("project_label", "") for t in selected_tools)
    scope_idx = radio_menu(
        "Where to install?",
        ["Global", "This project", "Other path"],
        [
            f"all projects  →  {global_paths}",
            f"here only     →  {project_paths}",
            "specify a directory",
        ],
    )

    if scope_idx == 0:
        scope = "global"
        project_dir = None
    elif scope_idx == 1:
        scope = "project"
        project_dir = Path.cwd()
        print(f"  Project: {cyan(str(project_dir))}")
    else:
        scope = "project"
        sys.stdout.write(f"\n  {bold('Project path:')} ")
        sys.stdout.flush()
        try:
            raw = input("").strip()
        except (EOFError, KeyboardInterrupt):
            sys.exit(0)
        project_dir = Path(raw).expanduser().resolve()
        if not project_dir.exists():
            print(red(f"  Path not found: {project_dir}"))
            sys.exit(1)
        print(f"  Project: {cyan(str(project_dir))}")

    # ── Step 3: Select skills ────────────────────────────────────────────────
    # Context-file-only tools (gemini, opencode) don't need skill selection
    skill_tools = [t for t in selected_tools if t.get("files_per_skill")]
    context_tools = [t for t in selected_tools if not t.get("files_per_skill")]

    selected_skills = []
    if skill_tools:
        skill_items = [(name, desc) for name, desc in SKILLS]
        sel_skill_idx = checkbox_menu("Select skills to install:", skill_items, set(range(len(SKILLS))))
        selected_skills = [SKILL_NAMES[i] for i in sorted(sel_skill_idx)]

        if not selected_skills and not context_tools:
            print(red("\n  No skills selected. Exiting."))
            sys.exit(0)

    # ── Step 4: Preview ──────────────────────────────────────────────────────
    print(f"\n{bold('  Preview:')}")
    print(f"  Tools:  {', '.join(t['name'] for t in selected_tools)}")
    print(f"  Scope:  {scope}" + (f" → {project_dir}" if project_dir else ""))
    if selected_skills:
        print(f"  Skills: {', '.join(selected_skills)}")
    if context_tools:
        print(f"  Context files for: {', '.join(t['name'] for t in context_tools)}")
    if args.dry_run:
        print(f"\n  {yellow('DRY RUN — no files will be written.')}")

    print()
    action = "Uninstall" if args.uninstall else "Install"
    if not confirm(f"{action}?"):
        print("  Aborted.")
        sys.exit(0)

    # ── Step 5: Execute ──────────────────────────────────────────────────────
    print()
    errors = 0

    for tool in selected_tools:
        print(bold(f"\n  ── {tool['name']} ──"))

        if scope == "global":
            base = tool.get("global_dir")
            if base is None:
                print(f"  {yellow('!')} Global install not supported for {tool['name']}. Use project scope.")
                continue
        else:
            base = project_dir / tool["project_subdir"]

        # Skills-based install
        if tool.get("files_per_skill") and selected_skills:
            for skill in selected_skills:
                if args.uninstall:
                    lines = uninstall_skill(skill, base, args.dry_run)
                else:
                    lines = install_skill(skill, base, args.dry_run)
                for line in lines:
                    print(line)
                    if "ERROR" in line:
                        errors += 1

        # Context-file install
        if not tool.get("files_per_skill"):
            ctx = tool.get("context_file", "CLAUDE.md")
            if args.uninstall:
                dest = base / ctx
                if dest.exists():
                    if not args.dry_run:
                        dest.unlink()
                    print(f"  {red('removed')} {dim(str(dest))}")
                else:
                    print(f"  {dim('skip')}   {dim(str(base / ctx))} (not found)")
            else:
                lines = install_context_file(ctx, base, args.dry_run)
                for line in lines:
                    print(line)
                    if "ERROR" in line:
                        errors += 1

    # ── Summary ──────────────────────────────────────────────────────────────
    print()
    print(bold("  ── Summary ──"))
    if args.dry_run:
        print(f"  {yellow('Dry run complete. No files written.')}")
    elif errors:
        print(f"  {yellow('Done with')} {red(str(errors))} {yellow('error(s).')} Check output above.")
    else:
        verb = "Uninstalled" if args.uninstall else "Installed"
        print(f"  {green(f'{verb} successfully.')}")

    if not args.uninstall and not args.dry_run and not errors:
        if any(t["id"] == "claude" for t in selected_tools):
            print(f"\n  Claude Code skills available as:")
            for skill in (selected_skills or []):
                print(f"    {dim('/')}dev-workflows:{skill}")
        print(f"\n  {dim('Restart your agent to load new skills.')}")

if __name__ == "__main__":
    main()
