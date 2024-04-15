#!/bin/bash


python3.10 -m venv venv
echo 'export PYTHONPATH="$PWD:$PYTHONPATH"' >> venv/bin/activate
source venv/bin/activate
pip install -r requirements.txt

echo "All done!"
