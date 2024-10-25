from rest_framework import pagination
from rest_framework.response import Response


class VirtualTruckPagination(pagination.PageNumberPagination):
    page_size_query_param = "page_size"

    def paginate_queryset(self, queryset, request, view=None):
        page_size = self.get_page_size(request)

        if not page_size:
            return None

        pagination = self.django_paginator_class(queryset, page_size)
        page_number = request.query_params.get(self.page_query_param, 1)

        if int(page_number) > pagination.num_pages:
            request.query_params._mutable = True
            request.query_params[self.page_query_param] = pagination.num_pages
            request.query_params._mutable = False

        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data) -> Response:
        return Response(
            {
                "total": self.page.paginator.count,
                "num_pages": self.page.paginator.num_pages,
                "page_number": self.page.number,
                "page_size": self.page.paginator.per_page,
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "results": data,
            }
        )
