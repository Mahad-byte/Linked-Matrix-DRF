from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from comments.models import Comment
from notifications.models import Notification


@receiver(post_save, sender=Comment)
def comment_creation_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.author, text=f"Comment {instance.text} has been created"
        )


@receiver(post_delete, sender=Comment)
def comment_deletion_notification(sender, instance, **kwargs):
    Notification.objects.create(
        user=instance.user, text=f"Comment {instance.text} has been Deleted"
    )
