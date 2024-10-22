from rest_framework import serializers

from .models import ImageProfilePic


class ImageProfilePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProfilePic
        fields = "__all__"
