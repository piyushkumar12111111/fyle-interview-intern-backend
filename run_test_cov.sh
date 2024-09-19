#!/bin/bash

# to stop on first error
set -e

# Restore db to initial state
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/

# Run test coverage
pytest -v --cov-report html:htmlcov --cov-config=.coveragerc --cov=core