# Proyecto Python con GitHub Actions

Este repositorio contiene un proyecto Python simple con pruebas unitarias y una
pipeline de GitHub Actions que ejecuta los tests automáticamente cuando se hace
un `push` o `pull request` sobre la rama `main`.

## Ejecutar localmente

```bash
python -m pip install -r requirements.txt
pytest
```

## GitHub Actions

El workflow se encuentra en `.github/workflows/tests.yml` y realiza estos pasos:

1. Instala Python.
2. Instala las dependencias del proyecto.
3. Ejecuta las pruebas unitarias.

