#!/bin/bash

# we need to run this script in the context of PI, otherwise, we don't have authority of GUI
if [ "$(id -un)" != "pi" ]; then
    exec sudo -u pi $0 "$@"
fi

# we need to make environment variable
export DISPLAY:=0

# now execute your code
cd Documents
cd Twelve
cd twelve
cd qt
python3 twelveneu.py