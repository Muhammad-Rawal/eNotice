from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Notice

@receiver(post_save, sender=Notice)
def send_notice_email(sender, instance, created, **kwargs):
    if created:
        subject = f'New Notice: {instance.title}'
        message = f'A new notice has been published.\n\nTitle: {instance.title}\nMessage: {instance.message}'
        recipients = [user.email for user in User.objects.all() if user.email]
        
        send_mail(subject, message, 'raw*******@gmail.com', recipients)
