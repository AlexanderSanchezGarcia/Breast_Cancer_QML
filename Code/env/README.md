# Entornos reproducibles del pipeline

Este directorio conserva las exportaciones de los entornos usados por el
pipeline. `radiomics` cubre los modulos 2 y 3; `qml_cancer` cubre los modulos
4, 5, 6 y 7. Los archivos `environment-*.yml` son exportaciones de Conda sin
builds y los archivos `requirements-*.txt` son las instantaneas de `pip freeze`.

Desde el 2026-09-23 PyRadiomics esta instalado tambien en `qml_cancer`, compilado
desde el mismo commit. `radiomics` sigue siendo el entorno de referencia de los
modulos 2 y 3; `qml_cancer` puede importarlo y ejecutarlos igual. Se verifico que
las features extraidas en ambos entornos son identicas: diferencia relativa
maxima 0 en 100 extracciones.

## PyRadiomics

PyRadiomics no se puede instalar desde PyPI. El sdist 3.1.0 declara la version
`3.0.1a1` en `pyproject.toml`, frente a `3.1.0` en `PKG-INFO`. Ademas, su
`MANIFEST.in` indica `recursive-include src/radiomics *` aunque la ruta real es
`radiomics/src`; por ello el tarball omite los headers `cmatrices.h` y
`cshape.h` y no compila. Tampoco existe un paquete en conda-forge.

La instalacion correcta es compilar desde el repositorio de AIM-Harvard en el
commit `8ed579383b44806651c463d5e691f3b2b57522ab` (2025-06-16), que emplea
`scikit-build-core` y admite `numpy>=2.0`. Con el entorno de conda activado:

```bash
# 1. Codigo fuente en el commit exacto. GitHub no acepta `git fetch` con un
#    hash abreviado, por eso se clona sin blobs y se hace checkout local.
git clone --filter=blob:none --no-checkout https://github.com/AIM-Harvard/pyradiomics.git pyradiomics
cd pyradiomics
git checkout --detach 8ed579383b44806651c463d5e691f3b2b57522ab

# 2. Dependencias de compilacion y de ejecucion, con las versiones de los
#    entornos congelados. numpy NO se actualiza: la extension en C se compila
#    contra el numpy ya instalado (2.2.6), que cumple numpy>=2.0.
python -m pip install "scikit-build-core==1.0.3" "cmake==4.4.2" "ninja==1.13.0" \
    "setuptools_scm==10.2.1" "PyWavelets==1.8.0" "pykwalify==1.8.0"

# 3. Compilar e instalar sin aislar la compilacion y sin tocar dependencias
python -m pip install --no-build-isolation --no-deps .

# 4. Comprobar
python -c "import radiomics; from radiomics import cMatrices, cShape; print(radiomics.__version__)"
```

Dos detalles que hacian fallar la version anterior de este procedimiento:

- `git fetch --depth 1 origin 8ed5793` falla, porque GitHub solo permite pedir
  un commit por su hash completo.
- `setuptools_scm` es necesario para calcular la version durante la compilacion.
  Con `--no-build-isolation` no se instala solo, y sin el la compilacion se
  detiene en la preparacion de metadatos.

Ademas, se retiro `pip install --upgrade "numpy>=2.0"`, que habria actualizado
numpy a la ultima version disponible y podia romper la compatibilidad con el
stack de Qiskit.

La version que se reporta depende de como se clone el repositorio. Un clon
shallow no ve los tags, y `setuptools_scm` informa `0.1.dev1+g8ed579383`, como en
`radiomics`. Un clon completo o sin blobs informa `3.1.1.dev111+g8ed579383`, como
en `qml_cancer`. Las dos corresponden al mismo commit (`g8ed579383`). **Lo que
ancla la reproducibilidad es el commit, no el numero de version.**
