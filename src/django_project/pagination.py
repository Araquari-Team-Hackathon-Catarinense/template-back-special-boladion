from rest_framework import pagination
from rest_framework.response import Response


class VirtualTruckPagination(pagination.PageNumberPagination):
    page_size_query_param = "page_size"

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
