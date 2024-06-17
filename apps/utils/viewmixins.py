from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render

User = get_user_model()


class UserOwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = get_object_or_404(User, pk=kwargs.get("pk"))
        if request.user != obj:
            return render(request, "403.html", status=403)
        return super().dispatch(request, *args, **kwargs)
