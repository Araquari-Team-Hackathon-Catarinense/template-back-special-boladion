from django.db.models.signals import post_save
from django.dispatch import receiver

from core.company.infra.company_django_app.models import Company
from core.uploader.domain.generate_avatar import generate_avatar
from core.uploader.infra.uploader_django_app.models import Document


@receiver(post_save, sender=Company)
def create_avatar(sender, instance, created, **kwargs):
    if created:
        if instance.name is None or instance.avatar is not None:
            return
        file = generate_avatar(instance.name)
        avatar: Document = Document.objects.create(
            description=f"{instance.name}'s avatar", type="AVATAR", file=file
        )
        avatar.save()
        instance.avatar = avatar
        instance.save()
