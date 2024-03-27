#!/bin/bash
echo "Creating virtual environment"
python3 -m venv .venv
source .venv/bin/activate
echo "Installing dependencies"
.venv/bin/pip install -r requirements.txt
echo "Installing bin script to PATH"
ln -s $(pwd)/bin_script/pyquranic-dl $HOME/.local/bin/pyquranic-dl
