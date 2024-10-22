import uuid

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from ...domain.generate_user_pic import generate_user_pic


def upload_image_fomater(filename, instance):
    return f"{str(uuid.uuid4())}-{filename}.png"


class ImageProfilePic(models.Model):
    image = models.ImageField(upload_to=upload_image_fomater, null=True, blank=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)


@receiver(post_save, sender=ImageProfilePic)
def create_image_profile_pic(instance, created, **kwargs):
    if created:
        if len(str(instance.image)) > 0:
            return
        else:
            image = generate_user_pic(instance.user_name)
            instance.image = image
            instance.save()
