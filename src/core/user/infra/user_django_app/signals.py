from django.db.models.signals import post_save
from django.dispatch import receiver

from core.image.infra.image_django_app.models import ImageProfilePic
from core.user.infra.user_django_app.models import User


@receiver(post_save, sender=User)
def create_pic(sender, instance, created, **kwargs):
    if created:
        print(instance.name)
        if instance.is_staff or instance.name is None:
            return
        pic = ImageProfilePic.objects.create(user_name=instance.name)
        instance.pic = pic
        instance.save()
