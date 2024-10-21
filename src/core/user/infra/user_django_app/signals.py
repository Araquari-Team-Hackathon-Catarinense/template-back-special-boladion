from django.db.models.signals import post_save
from django.dispatch import receiver

from core.user.infra.user_django_app.models import User
from core.image.infra.image_django_app.models import ImageProfilePic

@receiver(post_save, sender=User)
def create_pic(sender, instance, created, **kwargs):
    if created:
        pic: ImageProfilePic = ImageProfilePic.objects.create(user_name=instance.name)
        instance.pic = pic
        instance.save()