from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from .utils.sms_utils import send_sms_alert

@receiver(post_save, sender=Order)
def send_order_confirmation_sms(sender, instance, created, **kwargs):
    if created:
        message = f"Hi {instance.customer.name}, your order for {instance.item} has been placed successfully."
        send_sms_alert(instance.customer.phone_number, message)
