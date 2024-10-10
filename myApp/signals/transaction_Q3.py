from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import User


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

