from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class User(AbstractUser):
    # username field overwriting : blank=True
    username = models.CharField(max_length=30, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)

    name = models.CharField(max_length=30)
    img_profile = models.ImageField(upload_to='user', blank=True, null=True)
    phone_num = models.CharField(max_length=20, blank=True)
    # phone_num = models.CharField(max_length=20, unique=True)

    is_host = models.BooleanField(default=False)
    is_facebookuser = models.BooleanField(default=False)

    def __str__(self):
        return ''

# @receiver(pre_save, sender=User)
# def save_email_to_username(sender, instance, using, **kwargs):
#     print('')
#     print(f'sender: {sender}')
#     print(f'instance: {instance}')
#     print(f'using: {using}')
#     print(f'**kwargs: {kwargs}')
#     print('')
#     # instance.file.delete(save=False)
#     instance.username = instance.email
#     instance.save()

# class FacebookUser(AbstractUser):
#     GENDER_CHOICES = (
#         ('m', 'male'),
#         ('w', 'female'),
#     )
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#     )
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
