# core/middleware.py
import logging
from django.utils import timezone

logger = logging.getLogger(__name__)

class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to execute for each request before the view (and later middleware) are called.
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        logger.info(f"{request.path} at {timezone.now()} and ip is {ip}")
        print("before")
        response = self.get_response(request)
        print("after")
        response["X-Custom-Header"] = "rafiq-samrat"

        # Code to execute for each request/response after the view is called.
        return response
