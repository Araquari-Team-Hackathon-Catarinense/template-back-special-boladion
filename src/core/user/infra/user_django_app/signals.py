from django.db.models.signals import post_save
from django.dispatch import receiver

from core.uploader.domain.generate_avatar import generate_avatar
from core.uploader.infra.uploader_django_app.admin import Document
from core.user.infra.user_django_app.models import User


@receiver(post_save, sender=User)
def create_avatar(sender, instance, created, **kwargs):
    if created:
        if instance.name is None or instance.avatar is not None or instance.is_staff:
            return
        file = generate_avatar(instance.name)
        avatar: Document = Document.objects.create(
            description=f"{instance.name}'s avatar", type="AVATAR", file=file
        )
        avatar.save()
        instance.avatar = avatar
        instance.save()
