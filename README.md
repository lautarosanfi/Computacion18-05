# Proyecto Python con Docker y GitHub Actions

Este repositorio contiene un proyecto Python simple con pruebas unitarias y una
pipeline de GitHub Actions que ejecuta los tests automaticamente dentro de un
contenedor Docker cuando se hace un `push` o `pull request` sobre la rama `main`.

## Ejecutar localmente sin Docker

```bash
python -m pip install -r requirements.txt
python -m pytest
```

## Ejecutar localmente con Docker

```bash
docker build -t computacion18-05-tests .
docker run --rm computacion18-05-tests
```

## GitHub Actions

El workflow se encuentra en `.github/workflows/tests.yml` y realiza estos pasos:

1. Descarga el codigo del repositorio.
2. Construye una imagen Docker del proyecto usando el `Dockerfile`.
3. Ejecuta automaticamente los tests dentro del contenedor.
4. Verifica el resultado usando el codigo de salida del comando `docker run`.

## Analisis

### Que ventajas aporta Docker en CI

Docker permite que los tests se ejecuten siempre en un entorno controlado y
reproducible. La version de Python, las dependencias y la forma de ejecutar el
proyecto quedan definidas en el `Dockerfile`, por lo que se reduce el riesgo de
que los tests pasen en una computadora pero fallen en otra por diferencias de
configuracion.

Tambien ayuda a detectar problemas relacionados con la construccion de la
aplicacion, porque la pipeline no solo ejecuta los tests: primero comprueba que
la imagen Docker pueda construirse correctamente.

### Que sucede cuando un test falla

Si un test falla, `pytest` termina con un codigo de salida distinto de cero.
Como `pytest` se ejecuta dentro del contenedor, ese error tambien hace fallar el
comando `docker run`.

GitHub Actions interpreta ese codigo de salida como un error del job y marca la
ejecucion de la pipeline como fallida.

### Como impacta esto en la pipeline

Cuando falla un test, la pipeline queda en rojo y el commit o pull request queda
marcado como no verificado. Si el repositorio tuviera reglas de proteccion de
rama, ese resultado podria impedir que se haga merge hasta corregir el problema.

Esto permite detectar errores automaticamente antes de integrar cambios a la
rama principal.

