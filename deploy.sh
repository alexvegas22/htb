#!/bin/bash
cd htb-backend/
. .venv/bin/activate
python -m flask --app main run &
cd ..
cd htb-frontend/
npm install
npm run dev &

