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
    form_classes = {
        "user_form": UserForm,
        "profile_form": UserProfileForm,
    }

    def get(self, request, *args, **kwargs):
        user_form = self.form_classes["user_form"](instance=request.user)
        profile_form = self.form_classes["profile_form"](instance=request.user.profile)
        return render(
            request,
            self.template_name,
            {
                "user_form": user_form,
                "profile_form": profile_form,
            },
        )

    def post(self, request, *args, **kwargs):
        user_form = self.form_classes["user_form"](request.POST, instance=request.user)
        profile_form = self.form_classes["profile_form"](request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, self.success_message)
            return redirect("users:user_detail", pk=request.user.pk)
        messages.error(request, _("Por favor, corrija os erros abaixo."))

        return render(
            request,
            self.template_name,
            {
                "user_form": user_form,
                "profile_form": profile_form,
            },
        )
