from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import User
import threading

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
