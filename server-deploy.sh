#!/bin/bash

cp .env htb-frontend/.env
cp .env api/.env
cp .env websocket/.env

redis-server &

python -m venv .venv
. .venv/bin/activate
pip install -r api/requirements.txt
cd api/
flask run --host=0.0.0.0 &

cd ..
cd websocket/
npm install
node index.js &

cd ..
cd htb-frontend/
npm install
npm run dev -- --host &

