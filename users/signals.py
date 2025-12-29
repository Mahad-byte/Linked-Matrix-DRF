from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from notifications.models import Notification
from users.models import User


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
