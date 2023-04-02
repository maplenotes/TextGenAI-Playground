#!/bin/bash

SERVER_HOME=$(cd $(dirname $0); pwd)

# python venv setup
if [ ! -d "$SERVER_HOME/venv" ]; then
    python3 -m venv venv
fi

# activate venv
source ./venv/bin/activate

# install requirements
pip install -r requirements.txt

# run server with uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000
