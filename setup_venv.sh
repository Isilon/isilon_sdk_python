#!/bin/bash

set -e

venv_path=".venv"

pip install virtualenv

if [ -f $venv_path ]
then
    echo "venv found, no need to create it"
else
    virtualenv $venv_path
fi

. $venv_path/bin/activate
python setup.py install

echo
echo "To activate the virtual environment run: . $venv_path/bin/activate"
