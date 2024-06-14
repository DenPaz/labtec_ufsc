from allauth.account.forms import AddEmailForm as AllauthAddEmailForm
from allauth.account.forms import ChangePasswordForm as AllauthChangePasswordForm
from allauth.account.forms import LoginForm as AllauthLoginForm
from allauth.account.forms import ReauthenticateForm as AllauthReauthenticateForm
from allauth.account.forms import ResetPasswordForm as AllauthResetPasswordForm
from allauth.account.forms import ResetPasswordKeyForm as AllauthResetPasswordKeyForm
from allauth.account.forms import SetPasswordForm as AllauthSetPasswordForm
from allauth.account.forms import SignupForm as AllauthSignupForm
from allauth.account.forms import UserTokenForm as AllauthUserTokenForm
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import User, UserProfile


class AddEmailForm(AllauthAddEmailForm):
    pass


class ChangePasswordForm(AllauthChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["oldpassword"].widget.attrs.update(
            {
                "type": "password",
                "class": "form-control",
                "placeholder": _("Senha antiga"),
                "autofocus": True,
            }
        )
        self.fields["password1"].widget.attrs.update(
            {
                "type": "password",
                "class": "form-control",
                "placeholder": _("Nova senha"),
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "type": "password",
                "class": "form-control",
                "placeholder": _("Confirmar nova senha"),
            }
        )


class LoginForm(AllauthLoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].widget.attrs.update(
            {
                "type": "email",
                "class": "form-control",
                "placeholder": _("E-mail"),
                "autofocus": True,
            }
        )
        self.fields["password"].widget.attrs.update(
            {
                "type": "password",
                "class": "form-control",
                "placeholder": _("Senha"),
            }
        )
        self.fields["remember"].widget.attrs.update(
            {
                "type": "checkbox",
                "id": "remember",
            }
        )
        self.fields["remember"].label = _("Lembrar-me")


class ResetPasswordForm(AllauthResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {
                "type": "email",
                "class": "form-control",
                "placeholder": _("E-mail"),
                "autofocus": True,
            }
        )


class ResetPasswordKeyForm(AllauthResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update(
            {
                "type": "password",
                "class": "form-control",
                "placeholder": _("Nova senha"),
                "autofocus": True,
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "type": "password",
                "class": "form-control",
                "placeholder": _("Confirmar senha"),
            }
        )


class SetPasswordForm(AllauthSetPasswordForm):
    pass


class SignupForm(AllauthSignupForm):
    first_name = forms.CharField(
        max_length=50,
    )
    last_name = forms.CharField(
        max_length=50,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {
                "type": "text",
                "class": "form-control",
                "placeholder": _("Nome"),
                "autofocus": True,
            }
        )
        self.fields["last_name"].widget.attrs.update(
            {
                "type": "text",
                "class": "form-control",
                "placeholder": _("Sobrenome"),
            }
        )
        self.fields["email"].widget.attrs.update(
            {
                "type": "email",
                "class": "form-control",
                "placeholder": _("E-mail"),
                "autofocus": True,
            }
        )
        self.fields["password1"].widget.attrs.update(
            {
                "type": "password",
                "class": "form-control",
                "placeholder": _("Senha"),
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "type": "password",
                "class": "form-control",
                "placeholder": _("Confirmar senha"),
            }
        )


class UserTokenForm(AllauthUserTokenForm):
    pass


class ReauthenticateForm(AllauthReauthenticateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget.attrs.update(
            {
                "type": "password",
                "class": "form-control",
                "placeholder": _("Senha"),
                "autofocus": True,
            }
        )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "curso",
            "nacionalidade",
            "data_nascimento",
            "foto_perfil",
            "modo_escuro",
        ]
        widgets = {
            "curso": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "nacionalidade": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "data_nascimento": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            "foto_perfil": forms.FileInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "modo_escuro": forms.CheckboxInput(),
        }
