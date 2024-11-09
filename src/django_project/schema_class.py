from drf_spectacular.openapi import AutoSchema
from drf_spectacular.utils import OpenApiParameter


class SchemaWithCompany(AutoSchema):
    global_params = [
        OpenApiParameter(
            name="X-Company-Id",
            type=str,
            location=OpenApiParameter.HEADER,
            description="`UUID of company Id",
            default="51134a9e-ab9b-4d4d-9b34-905250b459a1",
        )
    ]

    def get_override_parameters(self):
        params = super().get_override_parameters()
        return params + self.global_params
