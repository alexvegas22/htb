#!/bin/bash

python -m venv .venv
pip install -r api/requirements.txt
source .venv/bin/activate
flask run &

cd htb-frontend/
npm install
npm run dev &

