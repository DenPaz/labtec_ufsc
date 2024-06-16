from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.views.generic import DetailView, View

from .forms import UserForm, UserProfileForm
from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "users/user_detail.html"


class UserUpdateView(LoginRequiredMixin, View):
    template_name = "users/user_update.html"
    success_message = _("Perfil atualizado com sucesso!")

    def get_context_data(self, **kwargs):
        context = {
            "form_user": UserForm(instance=self.request.user),
            "form_profile": UserProfileForm(instance=self.request.user.profile),
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
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
