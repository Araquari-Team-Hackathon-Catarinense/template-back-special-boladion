from drf_spectacular.openapi import AutoSchema
from drf_spectacular.utils import OpenApiParameter


class SchemaWithCompany(AutoSchema):
    global_params = [
        OpenApiParameter(
            name="X-Company-Id",
            type=str,
            location=OpenApiParameter.HEADER,
            description="`UUID of company Id",
        )
    ]

    def get_override_parameters(self):
        params = super().get_override_parameters()
        return params + self.global_params
