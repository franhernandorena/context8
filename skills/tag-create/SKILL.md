---
name: tag-create
version: 1.0.0
description: Crea tags git basado en los cambios desde el último tag. Lee convenciones de .context8/repo-branches.md, analiza commits, sugiere el próximo número de versión (semver) y pide confirmación antes de crear.
---

# Tag Create — Creación de Tags Git

## Overview

Lee las convenciones del repositorio desde `.context8/repo-branches.md` (creado
por `repo-cleanup`), analiza los cambios desde el último tag, clasifica el tipo
de cambios (fix, feature, breaking), sugiere el próximo número de versión, y
pide confirmación antes de crear el tag con un mensaje descriptivo.

## Cuando usar

- Después de mergear cambios significativos
- Antes de un release
- Cuando quieres marcar un punto en la historia con un tag semver

## Output

- Tag creado en el repositorio local
- `.context8/repo-branches.md` actualizado con el nuevo tag
- Push del tag si el usuario lo autoriza

## Full Prompt

# TAG CREATE — Crear Tag Git

---

## Fase 1 — Cargar Convenciones del Repositorio

### 1.1 Leer tags existentes

```bash
git tag --sort=-creatordate | head -20
```

### 1.2 Leer `.context8/repo-branches.md`

```bash
cat .context8/repo-branches.md 2>/dev/null || echo "No existe — se creará al final"
```

Extraer: formato de tags usado históricamente (v0.0.0, v0-0-0, etc.),
y últimas versiones documentadas.

### 1.3 Último tag

```bash
LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "sin-tag")
echo "Último tag: $LAST_TAG"
```

---

## Fase 2 — Analizar Cambios Desde el Último Tag

### 2.1 Log de cambios

```bash
if [ "$LAST_TAG" != "sin-tag" ]; then
  git log "$LAST_TAG"..HEAD --oneline --no-decorate
else
  git log --oneline --no-decorate | tail -20
fi
```

### 2.2 Clasificar cambios

Leer cada mensaje de commit y clasificar:

| Tipo | Indicador | Ejemplo | Salto de versión |
|------|-----------|---------|-----------------|
| **Breaking** | `!`, `BREAKING CHANGE`, `feat!:` | `feat!: cambio de API` | Major (X+1.0.0) |
| **Feature** | `feat:`, `feature:`, `feat(` | `feat(auth): login con Google` | Minor (0.X+1.0) |
| **Fix** | `fix:`, `fix(`, `bugfix:`, `hotfix:` | `fix: null pointer en login` | Patch (0.0.X+1) |
| **Docs/Chore** | `docs:`, `chore:`, `refactor:`, `test:` | `docs: actualizar README` | Sin cambio |

### 2.3 Generar resumen de cambios

```
Commits desde v1.0.0 (5 commits):
  ✨ feat: login con Google
  🐛 fix: null pointer en login
  📚 docs: actualizar README
  ✨ feat: logout endpoint
  🔧 chore: limpiar dependencias

Clasificación:
  - Breaking:  0
  - Features:  2
  - Fixes:     1
  - Chore/doc: 2
```

---

## Fase 3 — Sugerir Próximo Tag

### 3.1 Calcular versión sugerida

Aplicar semver según la clasificación:

```
RAZONAMIENTO:
  Último tag: v1.0.0
  Breaking:  0 → no cambia major
  Features:  2 → sube minor (+1)
  Fixes:     1 → ignora (minor ya subió)

  Versión sugerida: v1.1.0
```

### 3.2 Respetar el formato histórico

Si los tags históricos usan `v0-0-0` (guiones), sugerir `v1-1-0`.
Si usan `v0.0.0` (puntos), sugerir `v1.1.0`.

### 3.3 Mostrar propuesta al usuario

```
═══ Propuesta de Tag ═══

  Tag sugerido:  v1.1.0
  Formato:       v<major>.<minor>.<patch> (semver)

  Commits desde v1.0.0:
    ✨ feat: login con Google
    🐛 fix: null pointer en login
    📚 docs: actualizar README
    ✨ feat: logout endpoint

  Mensaje sugerido:
    v1.1.0 — Nuevo login con Google, logout endpoint, fix null pointer

¿Confirmas?
  [Enter]      — crear tag con el nombre y mensaje sugerido
  <nombre>     — crear tag con otro nombre (escribe el que quieras)
  <mensaje>    — crear tag con el nombre sugerido pero otro mensaje
  skip         — cancelar
```

---

## Fase 4 — Crear Tag

### 4.1 Crear tag local

```bash
git tag -a <tag-name> -m "<tag-message>"
```

### 4.2 Verificar

```bash
git tag --sort=-creatordate | head -5
git log --oneline <tag-name> -1
```

### 4.3 Preguntar si hacer push

```
Tag v1.1.0 creado localmente.
¿Hago push al remoto?
  [y/N]
```

Si el usuario dice que sí:

```bash
git push origin <tag-name>
```

---

## Fase 5 — Actualizar `.context8/repo-branches.md`

Añadir el nuevo tag a la tabla de tags:

```markdown
| v1.1.0 | YYYY-MM-DD | Login con Google, logout endpoint, fix null pointer |
```

```bash
git add .context8/repo-branches.md
git commit -m "docs(repo-branches): añadir tag v1.1.0"
```

Solo hacer commit si el archivo existe.

---

## Rules

- Nunca crear un tag sin confirmación del usuario.
- El mensaje del tag debe ser descriptivo, no genérico como "release".
- Si no hay tags previos y no se puede determinar el formato, usar puntos (v0.1.0).
- Si no hay cambios desde el último tag, informar y no sugerir nada.
- Escribir toda la documentación en español.
