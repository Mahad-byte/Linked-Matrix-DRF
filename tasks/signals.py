from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from tasks.models import Task
from notifications.models import Notification


@receiver(post_save, sender=Task)
def task_creation_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.project.created_by,
            text=f"Task {instance.title} has been created",
        )


@receiver(post_delete, sender=Task)
def task_deletion_notification(sender, instance, **kwargs):
    Notification.objects.create(
        user=instance.project.created_by, text=f"Task {instance.title} has been Deleted"
    )
