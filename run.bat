@echo off
setlocal

set FLASK_APP=core/server.py
set FLASK_ENV=development

flask run --host=0.0.0.0 --port=5000