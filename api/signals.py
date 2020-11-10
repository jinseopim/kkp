from django.contrib.auth.models import User
from django.db.models.signals import post_save  # User 객체가 생성되면 시그널 정보를 전달
from django.dispatch import receiver  # 시그널 정보를 받는 리시버
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("Created:", created)    # 새롭게 객체 생성되면 True, 아니면 False

    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, user_pk=instance.id)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()