#!/bin/zsh

PKG_NAME="dac_energy_tutorial_07"

echo " >>> Create isolated Python environment ..."
rm -rf venv/ *.whl
python -m venv venv
source venv/bin/activate

python -m pip install -q -U pip setuptools wheel

echo " >>> Folder structure:"
tree -I 'venv|requirements.txt|demo.sh'

echo " >>> Install dac and requirements.txt ..."
python -m pip install -q dac -r requirements.txt

echo " >>> dac pack ..."
dac pack --load='load.py' --schema='schema.py' --pkg-dependencies="$(cat requirements.txt)" --pkg-name="${PKG_NAME}" --pkg-version='1.0.0'

echo " >>> Install the built package ${PKG_NAME}, with all its dependencies..."
python -m pip install -q *.whl

echo " >>> Execute with python \"from ${PKG_NAME}.load import load; print(load())\""
python -c "from ${PKG_NAME} import load; print(load())"

echo " >>> Execute with python \"from ${PKG_NAME}.load import Schema, load; print(load()[Schema.source].unique())\""
python -c "from ${PKG_NAME} import Schema, load; print(load()[Schema.source].unique())"

echo " >>> Execute with python \"from ${PKG_NAME} import Schema, load; import inspect; print(inspect.getsource(Schema))\""
python -c "from ${PKG_NAME} import Schema, load; import inspect; print(inspect.getsource(Schema))"

echo " >>> Execute with python \"from ${PKG_NAME} import load, Schema; print(Schema.validate(load(), lazy=True))\""
python -c "from ${PKG_NAME} import load, Schema; print(Schema.validate(load(), lazy=True))"

deactivate
