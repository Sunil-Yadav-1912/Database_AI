#!/bin/bash


# Set default values for Gunicorn options
WORKERS=2
BIND=0.0.0.0:5007
MODULE_NAME="app:app"  # Format: <module_name>:<application_instance>


# Change directory to the location of the Flask app
cd /Database_AI

# Run Gunicorn with specified options
exec gunicorn --workers $WORKERS --bind $BIND $MODULE_NAME