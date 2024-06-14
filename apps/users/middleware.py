from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class RedirectAuthenticatedUserMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.restricted_pages = {
            reverse("account_inactive"),
            reverse("account_reset_password"),
            reverse("account_reset_password_done"),
            reverse("account_reset_password_from_key_done"),
        }
        self.get_response = get_response

    def process_request(self, request):
        if request.path in self.restricted_pages and request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
