#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Gather static styling files
python manage.py collectstatic --no-input

# Sync the cloud database
python manage.py migrate

#  ✅ WORKAROUND: Automatically create the admin superuser if it doesn't exist
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'AdminPass123')"
