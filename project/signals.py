from django.dispatch import receiver
from project.models import Project
from notifications.models import Notification
from django.db.models.signals import post_save, post_delete


@receiver(post_save, sender=Project)
def project_creation_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.created_by,
            text=f"Project {instance.title} has been created"
        )


@receiver(post_delete, sender=Project)
def project_deletion_notification(sender, instance, **kwargs):
    Notification.objects.create(
        user=instance.created_by,
        text=f"Project {instance.title} has been Deleted"
    )
