# Generated by Django 4.2.13 on 2024-06-18 04:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Computador",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "id",
                    models.PositiveIntegerField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "processador",
                    models.CharField(max_length=100, verbose_name="Processador"),
                ),
                (
                    "memoria_ram",
                    models.PositiveIntegerField(verbose_name="Memória RAM (GB)"),
                ),
                (
                    "placa_video",
                    models.CharField(max_length=100, verbose_name="Placa de vídeo"),
                ),
                (
                    "armazenamento",
                    models.PositiveIntegerField(verbose_name="Armazenamento"),
                ),
                (
                    "so_principal",
                    models.CharField(
                        choices=[("Windows", "Windows"), ("Linux", "Linux")],
                        max_length=10,
                        verbose_name="SO. principal",
                    ),
                ),
                (
                    "so_secundario",
                    models.CharField(
                        blank=True,
                        choices=[("Windows", "Windows"), ("Linux", "Linux")],
                        max_length=10,
                        verbose_name="SO. secundário",
                    ),
                ),
                (
                    "fone_ouvido",
                    models.BooleanField(
                        default=True, verbose_name="Inclui fone de ouvido?"
                    ),
                ),
                (
                    "danificado",
                    models.BooleanField(default=False, verbose_name="Esta danificado?"),
                ),
            ],
            options={
                "verbose_name": "Computador",
                "verbose_name_plural": "Computadores",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="MesaTrabalho",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "id",
                    models.PositiveIntegerField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("monitor", models.BooleanField(default=True, verbose_name="Monitor")),
                (
                    "mouse_pad",
                    models.BooleanField(default=True, verbose_name="Possui mouse pad?"),
                ),
                (
                    "fone_ouvido",
                    models.BooleanField(
                        default=True, verbose_name="Possui fone de ouvido?"
                    ),
                ),
            ],
            options={
                "verbose_name": "Mesa de trabalho",
                "verbose_name_plural": "Mesas de trabalho",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="OculusVR",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "id",
                    models.PositiveIntegerField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("modelo", models.CharField(max_length=100, verbose_name="Modelo")),
                ("marca", models.CharField(max_length=100, verbose_name="Marca")),
                (
                    "resolucao",
                    models.CharField(max_length=100, verbose_name="Resolução"),
                ),
                (
                    "danificado",
                    models.BooleanField(default=False, verbose_name="Esta danificado?"),
                ),
            ],
            options={
                "verbose_name": "Oculus de Realidade Virtual",
                "verbose_name_plural": "Oculus de Realidade Virtual",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="SalaReuniao",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "id",
                    models.PositiveIntegerField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("mesas", models.PositiveIntegerField(verbose_name="Número de mesas")),
                (
                    "cadeiras",
                    models.PositiveIntegerField(verbose_name="Número de cadeiras"),
                ),
                (
                    "projetor",
                    models.BooleanField(default=True, verbose_name="Possui projetor?"),
                ),
                (
                    "quadro",
                    models.BooleanField(default=True, verbose_name="Possui quadro?"),
                ),
            ],
            options={
                "verbose_name": "Sala de reunião",
                "verbose_name_plural": "Salas de reunião",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Tablet",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "id",
                    models.PositiveIntegerField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("modelo", models.CharField(max_length=100, verbose_name="Modelo")),
                ("marca", models.CharField(max_length=100, verbose_name="Marca")),
                ("tamanho_tela", models.FloatField(verbose_name="Tamanho da tela")),
                (
                    "so",
                    models.CharField(
                        choices=[("Android", "Android"), ("iOS", "iOS")],
                        max_length=10,
                        verbose_name="Sist. Operacional",
                    ),
                ),
                (
                    "armazenamento",
                    models.PositiveIntegerField(verbose_name="Armazenamento"),
                ),
                (
                    "danificado",
                    models.BooleanField(default=False, verbose_name="Esta danificado?"),
                ),
            ],
            options={
                "verbose_name": "Tablet",
                "verbose_name_plural": "Tablets",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="KitTablet",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "id",
                    models.PositiveIntegerField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "caneta",
                    models.BooleanField(default=True, verbose_name="Possui caneta?"),
                ),
                (
                    "teclado",
                    models.BooleanField(default=True, verbose_name="Possui teclado?"),
                ),
                (
                    "mouse",
                    models.BooleanField(default=True, verbose_name="Possui mouse?"),
                ),
                (
                    "danificado",
                    models.BooleanField(default=False, verbose_name="Esta danificado?"),
                ),
                (
                    "tablet",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="kit",
                        to="recursos.tablet",
                        verbose_name="Tablet",
                    ),
                ),
            ],
            options={
                "verbose_name": "Kit Tablet",
                "verbose_name_plural": "Kits Tablet",
                "ordering": ["id"],
            },
        ),
    ]
