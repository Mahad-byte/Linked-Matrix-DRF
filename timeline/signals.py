from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from timeline.models import Timeline
from notifications.models import Notification


@receiver(post_save, sender=Timeline)
def timeline_creation_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.project.created_by,
            text=f"Timeline {instance.time} has been created",
        )


@receiver(post_delete, sender=Timeline)
def timeline_deletion_notification(sender, instance, **kwargs):
    Notification.objects.create(
        user=instance.project.created_by,
        text=f"Timeline {instance.time} has been Deleted",
    )
