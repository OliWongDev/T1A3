#!/bin/bash
echo -n "Installing dependencies... "

pip install attrs==22.1.0
pip install english-words==1.1.0
pip install iniconfig==1.1.1
pip install packaging==21.3
pip install pick==2.0.0
pip install pluggy==1.0.0
pip install py==1.11.0
pip install pyparsing==3.0.9
pip install pytest==7.1.3
pip install tomli==2.0.1

echo -n "Install complete"

python3 main.py