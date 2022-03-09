from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from credapp.models import Employee

#clear cache after object save and del

@receiver(post_delete, sender=Employee, dispatch_uid='emp_deleted')
def object_post_delete_handler(sender, **kwargs):
    cache.delete('emp_objects')

@receiver(post_save, sender=Employee, dispatch_uid='post_updated')
def object_post_save_handler(sender, **kwargs):
    cache.delete('emp_objects')