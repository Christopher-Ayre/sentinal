#!/bin/bash
python -m pip install virtualenv
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt