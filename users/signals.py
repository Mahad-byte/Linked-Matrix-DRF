from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from users.models import User
from notifications.models import Notification


@receiver(post_save, sender=User)
def user_creation_notification(sender, instance, created, **kwargs):
    print("inside create user notify")
    if created:
        Notification.objects.create(
            user=instance, text=f"User {instance.email} has been created"
        )


@receiver(post_delete, sender=User)
def user_deletion_notification(sender, instance, **kwargs):
    Notification.objects.create(
        user=instance, text=f"User {instance.email} has been Deleted"
    )
