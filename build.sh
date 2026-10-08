#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Gather static styling files
python manage.py collectstatic --no-input

# Sync the cloud database
python manage.py migrate
