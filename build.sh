#! /bin/sh
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
$HOME/.local/bin/pip3 install --requirement requirements.txt --target . --upgrade
