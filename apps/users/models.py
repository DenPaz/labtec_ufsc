import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.templatetags.static import static
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from utils.models import BaseModel
from utils.validators import FileSizeValidator

from .constants import Cursos
from .managers import UserManager


class User(BaseModel, AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("ID"),
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name=_("Nome"),
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=_("Sobrenome"),
    )
    email = models.EmailField(
        unique=True,
        verbose_name=_("E-mail"),
    )
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    class Meta:
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return self.get_full_name()

    def clean(self):
        super().clean()
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        if self.is_superuser:
            self.is_staff = True
            self.is_active = True


class UserProfile(BaseModel):
    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name=_("Usuário"),
    )
    curso = models.CharField(
        max_length=50,
        choices=Cursos.choices,
        blank=True,
        verbose_name=_("Curso"),
    )
    nacionalidade = CountryField(
        blank=True,
        verbose_name=_("Nacionalidade"),
    )
    data_nascimento = models.DateField(
        blank=True,
        null=True,
        verbose_name=_("Data de nascimento"),
    )
    foto_perfil = models.ImageField(
        blank=True,
        validators=[FileSizeValidator(5)],
        upload_to="users/profile_pictures",
        help_text=_("Tamanho máximo: 5 MB."),
        verbose_name=_("Foto de perfil"),
    )
    modo_escuro = models.BooleanField(
        default=False,
        verbose_name=_("Modo escuro"),
    )

    class Meta:
        verbose_name = _("Perfil de usuário")
        verbose_name_plural = _("Perfis de usuários")
        ordering = ["user__first_name", "user__last_name"]

    def __str__(self):
        return self.user.get_full_name()

    def get_profile_picture(self):
        if self.foto_perfil and hasattr(self.foto_perfil, "url"):
            return self.foto_perfil.url
        return static("images/default_user.png")

    def get_theme_display(self):
        return "dark" if self.modo_escuro else "white"
