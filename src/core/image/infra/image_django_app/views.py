from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.user.infra.user_django_app.models import User

from .models import ImageProfilePic
from .serializers import ImageProfilePicSerializer


class ImageProfilePicViewSet(ModelViewSet):
    queryset = ImageProfilePic.objects.all()
    serializer_class = ImageProfilePicSerializer


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def change_profile_pic(request):
    user_id = request.data.get("user_id")
    image = request.FILES.get("image")

    if user_id and image:
        user = User.objects.get(id=user_id)

        image_to_delete: ImageProfilePic = user.pic.id

        image = ImageProfilePic.objects.create(image=image)
        image.save()

        user.pic = image
        user.save()

        image = ImageProfilePic.objects.get(id=image_to_delete)
        image.delete()

        return Response(
            {"message": "Profile picture updated"}, status=status.HTTP_200_OK
        )
