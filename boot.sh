#!/bin/sh
. venv/bin/activate
python libs.py
exec gunicorn -b :5000 --access-logfile - --error-logfile - flask_app:app
