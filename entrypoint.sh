#!/bin/bash

# Perform initialization of table 'activities' inside PostgreSQL database
python main.py create-table

# Start the main application process
exec "$@"