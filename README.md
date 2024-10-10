# Django Signal and Python

## Project Description

This repository contains the code for an assessment on Django signals and custom Python classes. It demonstrates understanding of Django's signal system, database transactions, and Python class creation with specific requirements.

1. **Synchronous Signal Handling**: Django signals are executed synchronously by default.The demonstrate code is located in `myApp/signals/sync_Q1.py`. 
2. **Thread-aware Signal Handling**: Yes, by default, Django signals run in the same thread as the caller. Example code is in `myApp/signals/thread_Q2.py`. 
3. **Transactional Signal Handling**: Yes, by default, Django signals run in the same database transaction as the caller. It prove in demonstrates in `myApp/signals/transaction_Q3.py`. 
4. **Rectangle Class**: The `myApp/signals/rectangle.py` file contains a custom Rectangle class that meets the following requirements:
    - Initializes with length and width (both integers)
    - Can be iterated over
    - When iterated, yields length and width in specified dictionary formats


## Installation

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  

# Install Django
pip install django

# Create a new Django project (if not already created)
django-admin startproject Testing_project
cd Testing_project

# Create a new app (if not already created)
python manage.py startapp myApp

# Add the app to your settings.py
INSTALLED_APPS = [
    ...
    'myApp',
]

# Run migrations to create the necessary database tables
python manage.py makemigrations
python manage.py migrate
```
## Uses

```bash
# Run the Django shell
python manage.py shell


from from myApp.signals.sync_Q1 import create_user
from from myApp.signals.sync_Q1 import create_user_with_signal


# Test synchronous signal handling
user = create_user(username="testuser", email="test@example.com")

# Test thread-aware signal handling
user = create_user(username="anotheruser", email="another@example.com")

# Test transactional signal handling
create_user_with_signal(username="erroruser", email="error@example.com")

```