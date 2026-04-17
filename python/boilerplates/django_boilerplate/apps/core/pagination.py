from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultsPagination(PageNumberPagination):
    """
    Default pagination for all API endpoints.

    Query params:
      ?page=2         → page number
      ?page_size=50   → override page size (max 100)

    Response shape:
      {
        "count":    123,
        "next":     "http://api.example.org/accounts/?page=3",
        "previous": "http://api.example.org/accounts/?page=1",
        "results":  [ ... ]
      }
    """
    page_size              = 20
    page_size_query_param  = "page_size"
    max_page_size          = 100
    page_query_param       = "page"

    def get_paginated_response(self, data):
        return Response({
            "count":    self.page.paginator.count,
            "next":     self.get_next_link(),
            "previous": self.get_previous_link(),
            "total_pages": self.page.paginator.num_pages,
            "current_page": self.page.number,
            "results":  data,
        })

    def get_paginated_response_schema(self, schema):
        return {
            "type": "object",
            "properties": {
                "count":        {"type": "integer"},
                "next":         {"type": "string", "nullable": True},
                "previous":     {"type": "string", "nullable": True},
                "total_pages":  {"type": "integer"},
                "current_page": {"type": "integer"},
                "results":      schema,
            },
        }


class LargeResultsPagination(PageNumberPagination):
    """Use for export or admin-style endpoints that need more results."""
    page_size     = 100
    max_page_size = 1000


class CursorPagination(PageNumberPagination):
    """
    Cursor-based pagination for feeds / timelines.
    More efficient on large datasets than page-number pagination.
    """
    from rest_framework.pagination import CursorPagination as _Cursor
    ordering   = "-created_at"
    page_size  = 20
    cursor_query_param = "cursor"
