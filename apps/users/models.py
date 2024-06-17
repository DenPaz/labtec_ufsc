from django.contrib.auth.models import AbstractUser
from django.db import models
from django.templatetags.static import static
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from utils.validators import FileSizeValidator

from .constants import Cursos
from .managers import UserManager


class User(AbstractUser):
    id = models.AutoField(
        verbose_name=_("ID"),
        primary_key=True,
    )
    first_name = models.CharField(
        verbose_name=_("Nome"),
        max_length=50,
    )
    last_name = models.CharField(
        verbose_name=_("Sobrenome"),
        max_length=50,
    )
    email = models.EmailField(
        verbose_name=_("E-mail"),
        unique=True,
    )
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    class Meta:
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")

    def __str__(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def clean(self):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        self.is_active = True if self.is_superuser else self.is_active
        self.is_staff = True if self.is_superuser else self.is_staff

    def get_absolute_url(self):
        return reverse("users:user_detail", kwargs={"pk": self.pk})

    def get_user_role(self):
        if self.is_superuser:
            return _("Administrador")
        if self.is_staff:
            return _("Professor")
        return _("Aluno")


class UserProfile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name=_("Usuário"),
        primary_key=True,
    )
    curso = models.CharField(
        verbose_name=_("Curso"),
        choices=Cursos.choices,
        max_length=10,
        blank=True,
    )
    nacionalidade = CountryField(
        verbose_name=_("Nacionalidade"),
        blank=True,
    )
    data_nascimento = models.DateField(
        verbose_name=_("Data de nascimento"),
        blank=True,
        null=True,
    )
    foto_perfil = models.ImageField(
        verbose_name=_("Foto de perfil"),
        upload_to="users/profile_pictures",
        blank=True,
        help_text=_("Tamanho máximo: 5 MB."),
        validators=[FileSizeValidator(5)],
    )
    modo_escuro = models.BooleanField(
        verbose_name=_("Modo escuro"),
        default=False,
    )

    class Meta:
        verbose_name = _("Perfil de usuário")
        verbose_name_plural = _("Perfis de usuários")

    def __str__(self):
        return self.user.get_full_name()

    def get_absolute_url(self):
        return self.user.get_absolute_url()

    def get_profile_picture(self):
        if self.foto_perfil and hasattr(self.foto_perfil, "url"):
            return self.foto_perfil.url
        return static("images/default_user.png")

    def get_theme_display(self):
        return "dark" if self.modo_escuro else "white"
