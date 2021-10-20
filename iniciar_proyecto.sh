#!/bin/bash

source .env/bin/activate
cd src

export FLASK_APP=main.py
export FLASK_DEBUG=1
export FLASK_ENV=development

flask run
