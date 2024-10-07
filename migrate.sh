#!/bin/bash

# Run Django migrations
python manage.py migrate --noinput

# Optional: Collect static files (if you're using Django's static files management)
python manage.py collectstatic --noinput
