import logging
import time
import uuid

from django.utils.deprecation import MiddlewareMixin
from .request_id import set_request_id

logger = logging.getLogger("core.request")


class RequestIdLoggingMiddleware(MiddlewareMixin):
    header_name = "HTTP_X_REQUEST_ID"  # django META key

    def process_request(self, request):
        request_id = request.META.get(self.header_name) or uuid.uuid4().hex
        request.request_id = request_id
        set_request_id(request_id)

        request._start_time = time.perf_counter()

    def process_response(self, request, response): 
        duration_ms = -1.0

        if hasattr(request, "_start_time"):
            duration_ms = (time.perf_counter() - request._start_time) * 1000

        request_id = getattr(request, "request_id", None)
        if request_id:
            response["X-Request-ID"] = request_id

        logger.info(
            "method=%s path=%s status=%s duration_ms=%.2f",
            getattr(request, "method", "-"),
            getattr(request, "path", "-"),
            response.status_code,
            duration_ms,
        )

        return response

    def process_exception(self, request, exception):
        logger.exception("Unhandled exception")
        return None
