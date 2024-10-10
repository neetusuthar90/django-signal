# Django Signal and Python

## Project Description

This repository contains the code for an assessment on Django signals and custom Python classes. It demonstrates understanding of Django's signal system, database transactions, and Python class creation with specific requirements.

1. **Synchronous Signal Handling**: Django signals are executed synchronously by default.The demonstrate code is located in `myApp/signals/sync_Q1.py`. 

```bash

@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f"Signal handler started at {timezone.now()}")
        time.sleep(5)  # Simulates long-running task
        print(f"Signal handler finished at {timezone.now()}")

def create_user(username, email):
    start_time = timezone.now()
    print(f"Starting user creation at {start_time}")
    
    user = User.objects.create(username=username, email=email)
    
    end_time = timezone.now()
    print(f"User creation finished at {end_time}")
    print(f"Total time taken: {end_time - start_time}")
    return user

```

2. **Thread-aware Signal Handling**: Yes, by default, Django signals run in the same thread as the caller. Example code is in `myApp/signals/thread_Q2.py`. 

```bash

@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        current_thread = threading.current_thread()
        print(f"Signal handler running in thread: {current_thread.name}")

def create_user(username, email):
    current_thread = threading.current_thread()
    print(f"User creation running in thread: {current_thread.name}")
    
    user = User.objects.create(username=username, email=email)
    return user


```

3. **Transactional Signal Handling**: Yes, by default, Django signals run in the same database transaction as the caller. It prove in demonstrates in `myApp/signals/transaction_Q3.py`. 

```bash 

@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f"Signal: Attempting to create user log for {instance.username}")
        raise Exception("Signal: Simulated error in signal handler")

def create_user_with_signal(username, email):
    try:
        with transaction.atomic():
            user = User.objects.create(username=username, email=email)
            print(f"Main: User created: {user.username}")
    except Exception as e:
        print(f"Main: Error occurred: {str(e)}")

    user_exists = User.objects.filter(username=username).exists()
    print(f"Main: User {username} exists in database: {user_exists}")

```

4. **Rectangle Class**: The `myApp/signals/rectangle.py` file contains a custom Rectangle class that meets the following requirements:
    - Initializes with length and width (both integers)
    - Can be iterated over
    - When iterated, yields length and width in specified dictionary formats

```bash 

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}


rectangle = Rectangle(5, 10)

for dimension in rectangle:
    print(dimension)


```

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