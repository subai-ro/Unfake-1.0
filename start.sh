#!/bin/bash
export PYTHONPATH=/opt/render/project/src
gunicorn --bind 0.0.0.0:$PORT wsgi:app 