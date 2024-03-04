#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
.venv/bin/pip install -r requirements.txt
ln -s $(pwd)/run $HOME/.local/bin/quranic-audio-downloader
