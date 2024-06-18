from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render

User = get_user_model()


class UserOwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = get_object_or_404(User, pk=kwargs.get("pk"))
        if request.user != obj:
            return HttpResponseForbidden(render(request, "403.html"))
        return super().dispatch(request, *args, **kwargs)
