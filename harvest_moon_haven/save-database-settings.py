# Near the top of settings.py...

# Add this import
import os

# This line already exists
from pathlib import Path

# Add these 3 lines of code
import environ
environ.Env()
environ.Env.read_env()


# Then...
# Replace DATABASES with this
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'harvest_moon_haven',
    'USER': os.environ['DB_USER'],
    'PASSWORD': os.environ['DB_PW'],
    'HOST': os.environ['DB_HOST'],
    'PORT': '5432',
  }
}