#!/bin/bash
export PYTHONPATH=/opt/render/project/src
/opt/render/project/src/.venv/bin/gunicorn --bind 0.0.0.0:$PORT wsgi:app 