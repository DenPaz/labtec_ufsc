from django.contrib.auth import get_user_model
from django.shortcuts import render

User = get_user_model()


class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not isinstance(obj, User):
            obj = obj.user
        if request.user != obj:
            return render(request, "403.html", status=403)
        return super().dispatch(request, *args, **kwargs)
