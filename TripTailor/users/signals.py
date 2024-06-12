from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signal to create a Profile instance whenever
    a new User instance is created.

    This function listens to the `post_save` signal
    from the User model. When a new user is created,
    it automatically creates a corresponding Profile instance.

    Args:
        sender (Model): The model class that sent the signal (User model).
        instance (User): The actual instance being saved.
        created (bool): A boolean indicating whether a
        new record was created.
        **kwargs: Additional keyword arguments.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Signal to save the Profile instance whenever
    the User instance is saved.

    This function listens to the `post_save` signal
    from the User model. When a user is saved,
    it automatically saves the corresponding Profile instance.

    Args:
        sender (Model): The model class that sent the signal (User model).
        instance (User): The actual instance being saved.
        **kwargs: Additional keyword arguments.
    """
    instance.profile.save()