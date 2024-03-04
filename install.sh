#!/bin/bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
ln -s $(pwd)/run $HOME/.local/bin/quranic-audio-downloader
