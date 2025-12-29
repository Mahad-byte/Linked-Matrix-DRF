from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from profiles.models import Profile
from notifications.models import Notification


@receiver(post_save, sender=Profile)
def profile_creation_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.user, text=f"Profile {instance.role} has been created"
        )


@receiver(post_delete, sender=Profile)
def profile_deletion_notification(sender, instance, **kwargs):
    Notification.objects.create(
        user=instance.user, text=f"Profile {instance.role} has been Deleted"
    )
