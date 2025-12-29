from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from documents.models import Document
from notifications.models import Notification


@receiver(post_save, sender=Document)
def document_creation_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.project.created_by,
            text=f"Document {instance.name} has been created",
        )


@receiver(post_delete, sender=Document)
def document_deletion_notification(sender, instance, **kwargs):
    Notification.objects.create(
        user=instance.project.created_by,
        text=f"Document {instance.name} has been Deleted",
    )
