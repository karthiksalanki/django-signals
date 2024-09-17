# user_signals/signals.py
from rest_framework.response import Response
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import status
from django.db import transaction
import threading

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    try:
        with transaction.atomic():
            print(f"Signal handler called in thread: {threading.current_thread().name}")
            if created:
                send_mail(
                    'Welcome to Our Platform',
                    'Thank you for signing up!',
                    settings.EMAIL_HOST_USER,
                    [instance.email],
                    fail_silently=False,
                )
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

