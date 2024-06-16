# Generated by Django 4.2.13 on 2024-06-16 22:40

import apps.users.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import utils.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50, verbose_name="Nome")),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Sobrenome"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="E-mail"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Usuário",
                "verbose_name_plural": "Usuários",
            },
            managers=[
                ("objects", apps.users.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="profile",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuário",
                    ),
                ),
                (
                    "curso",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("EC", "Engenharia de Computação"),
                            ("EE", "Engenharia de Energia"),
                            ("FISIO", "Fisioterapia"),
                            ("MED", "Medicina"),
                            ("TIC", "Tecnologias da Informação e Comunicação"),
                        ],
                        max_length=10,
                        verbose_name="Curso",
                    ),
                ),
                (
                    "nacionalidade",
                    django_countries.fields.CountryField(
                        blank=True, max_length=2, verbose_name="Nacionalidade"
                    ),
                ),
                (
                    "data_nascimento",
                    models.DateField(
                        blank=True, null=True, verbose_name="Data de nascimento"
                    ),
                ),
                (
                    "foto_perfil",
                    models.ImageField(
                        blank=True,
                        help_text="Tamanho máximo: 5 MB.",
                        upload_to="users/profile_pictures",
                        validators=[utils.validators.FileSizeValidator(5)],
                        verbose_name="Foto de perfil",
                    ),
                ),
                (
                    "modo_escuro",
                    models.BooleanField(default=False, verbose_name="Modo escuro"),
                ),
            ],
            options={
                "verbose_name": "Perfil de usuário",
                "verbose_name_plural": "Perfis de usuários",
            },
        ),
    ]
