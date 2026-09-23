# Entornos reproducibles del pipeline

Este directorio conserva las exportaciones de los entornos usados por el
pipeline. `radiomics` cubre los modulos 2 y 3; `qml_cancer` cubre los modulos
4, 5, 6 y 7. Los archivos `environment-*.yml` son exportaciones de Conda sin
builds y los archivos `requirements-*.txt` son las instantaneas de `pip freeze`.

## PyRadiomics

PyRadiomics no se puede instalar desde PyPI. El sdist 3.1.0 declara la version
`3.0.1a1` en `pyproject.toml`, frente a `3.1.0` en `PKG-INFO`. Ademas, su
`MANIFEST.in` indica `recursive-include src/radiomics *` aunque la ruta real es
`radiomics/src`; por ello el tarball omite los headers `cmatrices.h` y
`cshape.h` y no compila. Tampoco existe un paquete en conda-forge.

La instalacion correcta es compilar desde el repositorio de AIM-Harvard en el
commit `8ed5793`, que emplea `scikit-build-core` y admite `numpy>=2.0`:

```bash
git clone --no-checkout https://github.com/AIM-Harvard/pyradiomics.git pyradiomics
cd pyradiomics
git fetch --depth 1 origin 8ed5793
git checkout --detach FETCH_HEAD
python -m pip install --upgrade "numpy>=2.0" scikit-build-core
python -m pip install --no-build-isolation .
```

La version instalada se reporta como `0.1.dev1+g8ed579383` porque el clon es
shallow y `setuptools_scm` no puede ver los tags. La referencia que ancla la
reproducibilidad es el COMMIT `8ed5793`, no ese numero de version.
