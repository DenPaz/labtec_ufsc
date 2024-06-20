from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render

User = get_user_model()


class UserOwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = get_object_or_404(User, pk=kwargs.get("pk"))
        if request.user != obj:
            return HttpResponseForbidden(render(request, "403.html"))
        return super().dispatch(request, *args, **kwargs)


class StaffuserRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden(render(request, "403.html"))
        return super().dispatch(request, *args, **kwargs)


class SuperuserRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden(render(request, "403.html"))
        return super().dispatch(request, *args, **kwargs)


class SearchMixin:
    search_fields = []

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        if search:
            query = Q()
            for field in self.search_fields:
                query |= Q(**{f"{field}__icontains": search})
            queryset = queryset.filter(query)
        return queryset
