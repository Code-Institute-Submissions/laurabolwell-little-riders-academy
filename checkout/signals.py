from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import BookingItem


@receiver(post_save, sender=BookingItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update booking total when a booking items is updated/created
    """
    instance.booking.update_total()


@receiver(post_delete, sender=BookingItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update booking total when a booking item is deleted
    """
    instance.booking.update_total()
