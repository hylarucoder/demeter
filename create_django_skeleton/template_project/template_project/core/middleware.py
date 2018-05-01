import time
from django.conf import settings
from django.urls import get_urlconf, set_urlconf
from django.utils.deprecation import MiddlewareMixin


class XForwardedForMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.META.get("HTTP_X_FORWARDED_FOR", False):
            request.META["HTTP_X_PROXY_REMOTE_ADDR"] = request.META["REMOTE_ADDR"]
            parts = request.META["HTTP_X_FORWARDED_FOR"].split(",", 1)
            request.META["REMOTE_ADDR"] = parts[0]


class HostsRequestResponseMiddleware(MiddlewareMixin):
    def process_request(self, request):
        host = request.get_host()
        for sub_domain, urlconf in settings.SUB_DOMAINS_URLCONF.items():
            if host.split('.')[0] == sub_domain:
                # This is the main part of this middleware
                request.urlconf = urlconf
                request.host = host

    def process_response(self, request, response):
        host = request.get_host()
        for sub_domain, urlconf in settings.SUB_DOMAINS_URLCONF.items():
            if host.split('.')[0] == sub_domain:
                # This is the main part of this middleware
                request.urlconf = urlconf
                request.host = host
        return response
