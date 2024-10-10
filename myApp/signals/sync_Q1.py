from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from ..models import User
import time

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
