import json


class CompanyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.company_id = request.headers.get("X-Company-Id", None)

        if request.method in ["POST", "PUT", "PATCH"]:
            if request.content_type == "application/json":
                body = json.loads(request.body)
                if body.get("company") is None:
                    body["company"] = request.company_id
                    request._body = json.dumps(body).encode("utf-8")
                    request.META["CONTENT_LENGTH"] = len(request._body)
                print(request.body)

        response = self.get_response(request)

        return response
