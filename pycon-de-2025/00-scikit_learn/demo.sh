#!/bin/zsh

echo " >>> Create isolated Python environment ..."
rm -rf venv/
python -m venv venv
source venv/bin/activate

python -m pip install -q -U pip setuptools wheel
python -m pip install -r requirements.txt

python sklearn_dataset.py

deactivate
