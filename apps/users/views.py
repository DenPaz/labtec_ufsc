from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext as _
from django.views.generic import DetailView, View
from utils.viewmixins import UserIsOwnerMixin

from .forms import UserForm, UserProfileForm
from .models import User


class UserDetailView(LoginRequiredMixin, UserIsOwnerMixin, DetailView):
    model = User
    template_name = "users/user_detail.html"


class UserUpdateView(LoginRequiredMixin, UserIsOwnerMixin, View):
    template_name = "users/user_update.html"
    success_message = _("Perfil atualizado com sucesso!")

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs["pk"])

    def get(self, request, *args, **kwargs):
        context = {
            "form_user": UserForm(instance=request.user),
            "form_profile": UserProfileForm(instance=request.user.profile),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form_user = UserForm(request.POST, instance=request.user)
        form_profile = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        context = {
            "form_user": form_user,
            "form_profile": form_profile,
        }
        if form_user.is_valid() and form_profile.is_valid():
            form_user.save()
            form_profile.save()
            messages.success(request, self.success_message)
            return redirect("users:user_detail", pk=request.user.pk)
        return render(request, self.template_name, context)
