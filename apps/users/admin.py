from allauth.account.decorators import secure_admin_login
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import UserProfile

User = get_user_model()

if settings.DJANGO_ADMIN_FORCE_ALLAUTH:
    admin.autodiscover()
    admin.site.login = secure_admin_login(admin.site.login)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (
            _("Credenciais de login"),
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Informações pessoais"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissões"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("Datas importantes"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            _("Credenciais de login"),
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
        (
            _("Informações pessoais"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                ),
            },
        ),
    )
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "last_login",
        "date_joined",
    )
    list_filter = (
        "is_active",
        "is_staff",
        "is_superuser",
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
    ordering = (
        "first_name",
        "last_name",
    )
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    readonly_fields = (
        "last_login",
        "date_joined",
    )
    list_per_page = 10


@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    fieldsets = (
        (
            _("Informações do perfil"),
            {
                "fields": (
                    "user",
                    "curso",
                    "nacionalidade",
                    "data_nascimento",
                    "foto_perfil",
                    "modo_escuro",
                )
            },
        ),
    )
    list_display = (
        "user",
        "curso",
        "nacionalidade",
        "data_nascimento",
        "modo_escuro",
    )
    list_filter = ("curso",)
    search_fields = (
        "user__email",
        "user__first_name",
        "user__last_name",
    )
    ordering = ("user",)
    readonly_fields = ("user",)
    list_per_page = 10
