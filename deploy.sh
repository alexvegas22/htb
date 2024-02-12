#!/bin/bash
cd api/
. .venv/bin/activate
python -m flask run &
cd ..
cd htb-frontend/
npm install
npm run dev &

