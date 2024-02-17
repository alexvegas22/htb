#!/bin/bash

python -m venv .venv
pip install -r api/requirements.txt
. .venv/bin/activate
cd api/src/
flask run &

cd websocket/
npm install
node index.js &

cd ..
cd htb-frontend/
npm install
npm run dev &

