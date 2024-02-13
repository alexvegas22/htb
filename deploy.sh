#!/bin/bash
python -m venv .venv
source .venv/bin/activate
flask run &
cd htb-frontend/
npm install
npm run dev &

