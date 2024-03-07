#!/bin/bash

redis-server &

python -m venv .venv
. .venv/bin/activate
pip install -r api/requirements.txt
cd api/
flask run &

cd ..
cd websocket/
npm install
node index.js &



cd ..
cd htb-frontend/
npm install
npm run dev -- --host &

