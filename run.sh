#!/bin/bash

source ../env/bin/activate
export FLASK_APP=server.py
flask run -h 0.0.0.0 -p 12345