from django.http.response import HttpResponse
import jwt
import os
from dotenv import load_dotenv
load_dotenv()


class Authenticator:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if hasattr(request.headers, 'jwt') is False:
            return HttpResponse('<h1>You are not allowed, No Token Found</h1>')
        decoded = jwt.decode(request.headers.jwt,
                             "secret", algorithms=["HS256"])
        if decoded.body == os.getenv("SECRET_KEY"):
            response = self.get_response(request)
            return response
        else:
            return HttpResponse("<h1>Token Invalid</h1>")
