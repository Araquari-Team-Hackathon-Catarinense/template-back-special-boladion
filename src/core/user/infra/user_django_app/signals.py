from django.db.models.signals import post_save
from django.dispatch import receiver

from core.image.infra.image_django_app.models import ImageProfilePic
from core.uploader.domain.generate_user_pic import generate_user_pic
from core.uploader.infra.uploader_django_app.admin import Document
from core.user.infra.user_django_app.models import User


@receiver(post_save, sender=User)
def create_pic(sender, instance, created, **kwargs):
    if created:
        if instance.name is None or instance.avatar is not None:
            return
        file = generate_user_pic(instance.name)
        avatar: Document = Document.objects.create(
            description=f"{instance.name}'s avatar", type="AVATAR", file=file
        )
        avatar.save()
        instance.avatar = avatar
        instance.save()
