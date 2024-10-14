from core.company.infra.django_app.serializers import CompanyListSerializer
from rest_framework.viewsets import ModelViewSet

from .models import Company


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()

    def get_serializer_class(self):
        if self.action == "List":
            return CompanyListSerializer
        return CompanyListSerializer
