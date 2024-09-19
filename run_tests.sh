
#!/bin/bash

# to stop on first error
set -e

# Restore db to initial state
export FLASK_APP=core/server.py
rm -f core/store.sqlite3

# flask db init -d core/migrations/
#flask db migrate -m "Initial migration." -d core/migrations/
flask db upgrade -d core/migrations/

# Run tests
pytest -vvv -s tests/
pytest --cov