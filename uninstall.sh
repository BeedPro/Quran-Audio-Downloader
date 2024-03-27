#!/bin/bash
echo "Removing pyquranic-dl from PATH"
rm $HOME/.local/bin/pyquranic-dl
echo "Removing pyquranic-dl venv"
rm -r $(pwd)/.venv
