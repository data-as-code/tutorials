#!/bin/zsh

PKG_NAME="dac_energy_tutorial_05"

echo " >>> Create isolated Python environment ..."
rm -rf venv/
rm -rf dist/
rm -rf build/
python -m venv venv
source venv/bin/activate

python -m pip install -q -U pip setuptools wheel build

echo " >>> Folder structure:"
tree -I 'dist|venv|build|requirements.txt|*.egg-info|*.whl|demo.sh'

echo " >>> Build the package ..."
python -m build --wheel --outdir . . >/dev/null

echo " >>> Install the built package ${PKG_NAME}, with all its dependencies..."
python -m pip install -q *.whl

echo " >>> Execute with python \"from ${PKG_NAME}.load import load; print(load())\""
python -c "from ${PKG_NAME} import load; print(load())"

echo " >>> Execute with python \"from ${PKG_NAME}.load import Schema, load; print(load()[Schema.source].unique())\""
python -c "from ${PKG_NAME} import Schema, load; print(load()[Schema.source].unique())"

echo " >>> Execute with python \"from ${PKG_NAME} import Schema, load; import inspect; print(inspect.getsource(Schema))\""
python -c "from ${PKG_NAME} import Schema, load; import inspect; print(inspect.getsource(Schema))"

deactivate
