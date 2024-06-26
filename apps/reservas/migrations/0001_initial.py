# Generated by Django 4.2.13 on 2024-06-23 17:18

import apps.utils.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("recursos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReservaComputador",
            fields=[
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
                (
                    "data",
                    models.DateField(
                        validators=[apps.utils.validators.DateValidator()],
                        verbose_name="Data",
                    ),
                ),
                (
                    "horario",
                    models.CharField(
                        choices=[
                            ("1", "08:00 às 09:00"),
                            ("2", "09:00 às 10:00"),
                            ("3", "10:00 às 11:00"),
                            ("4", "11:00 às 12:00"),
                            ("5", "12:00 às 13:00"),
                            ("6", "13:00 às 14:00"),
                            ("7", "14:00 às 15:00"),
                            ("8", "15:00 às 16:00"),
                            ("9", "16:00 às 17:00"),
                            ("10", "17:00 às 18:00"),
                            ("11", "18:00 às 19:00"),
                            ("12", "19:00 às 20:00"),
                        ],
                        max_length=20,
                        verbose_name="Horário",
                    ),
                ),
            ],
            options={
                "verbose_name": "Reserva de computador",
                "verbose_name_plural": "Reservas de computadores",
                "ordering": ("data", "horario", "computador"),
            },
        ),
        migrations.CreateModel(
            name="ReservaKitTablet",
            fields=[
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
                (
                    "data",
                    models.DateField(
                        validators=[apps.utils.validators.DateValidator()],
                        verbose_name="Data",
                    ),
                ),
                (
                    "horario",
                    models.CharField(
                        choices=[
                            ("1", "08:00 às 09:00"),
                            ("2", "09:00 às 10:00"),
                            ("3", "10:00 às 11:00"),
                            ("4", "11:00 às 12:00"),
                            ("5", "12:00 às 13:00"),
                            ("6", "13:00 às 14:00"),
                            ("7", "14:00 às 15:00"),
                            ("8", "15:00 às 16:00"),
                            ("9", "16:00 às 17:00"),
                            ("10", "17:00 às 18:00"),
                            ("11", "18:00 às 19:00"),
                            ("12", "19:00 às 20:00"),
                        ],
                        max_length=20,
                        verbose_name="Horário",
                    ),
                ),
            ],
            options={
                "verbose_name": "Reserva de kit de tablet",
                "verbose_name_plural": "Reservas de kits de tablet",
                "ordering": ("data", "horario", "kit_tablet"),
            },
        ),
        migrations.CreateModel(
            name="ReservaMesaTrabalho",
            fields=[
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
                (
                    "data",
                    models.DateField(
                        validators=[apps.utils.validators.DateValidator()],
                        verbose_name="Data",
                    ),
                ),
                (
                    "horario",
                    models.CharField(
                        choices=[
                            ("1", "08:00 às 09:00"),
                            ("2", "09:00 às 10:00"),
                            ("3", "10:00 às 11:00"),
                            ("4", "11:00 às 12:00"),
                            ("5", "12:00 às 13:00"),
                            ("6", "13:00 às 14:00"),
                            ("7", "14:00 às 15:00"),
                            ("8", "15:00 às 16:00"),
                            ("9", "16:00 às 17:00"),
                            ("10", "17:00 às 18:00"),
                            ("11", "18:00 às 19:00"),
                            ("12", "19:00 às 20:00"),
                        ],
                        max_length=20,
                        verbose_name="Horário",
                    ),
                ),
            ],
            options={
                "verbose_name": "Reserva de mesa de trabalho",
                "verbose_name_plural": "Reservas de mesas de trabalho",
                "ordering": ("data", "horario", "mesa_trabalho"),
            },
        ),
        migrations.CreateModel(
            name="ReservaOculusVR",
            fields=[
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
                (
                    "data",
                    models.DateField(
                        validators=[apps.utils.validators.DateValidator()],
                        verbose_name="Data",
                    ),
                ),
                (
                    "horario",
                    models.CharField(
                        choices=[
                            ("1", "08:00 às 09:00"),
                            ("2", "09:00 às 10:00"),
                            ("3", "10:00 às 11:00"),
                            ("4", "11:00 às 12:00"),
                            ("5", "12:00 às 13:00"),
                            ("6", "13:00 às 14:00"),
                            ("7", "14:00 às 15:00"),
                            ("8", "15:00 às 16:00"),
                            ("9", "16:00 às 17:00"),
                            ("10", "17:00 às 18:00"),
                            ("11", "18:00 às 19:00"),
                            ("12", "19:00 às 20:00"),
                        ],
                        max_length=20,
                        verbose_name="Horário",
                    ),
                ),
            ],
            options={
                "verbose_name": "Reserva de Oculus VR",
                "verbose_name_plural": "Reservas de Oculus VR",
                "ordering": ("data", "horario", "oculus_vr"),
            },
        ),
        migrations.CreateModel(
            name="ReservaSalaReuniao",
            fields=[
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
                (
                    "data",
                    models.DateField(
                        validators=[apps.utils.validators.DateValidator()],
                        verbose_name="Data",
                    ),
                ),
                (
                    "horario",
                    models.CharField(
                        choices=[
                            ("1", "08:00 às 09:00"),
                            ("2", "09:00 às 10:00"),
                            ("3", "10:00 às 11:00"),
                            ("4", "11:00 às 12:00"),
                            ("5", "12:00 às 13:00"),
                            ("6", "13:00 às 14:00"),
                            ("7", "14:00 às 15:00"),
                            ("8", "15:00 às 16:00"),
                            ("9", "16:00 às 17:00"),
                            ("10", "17:00 às 18:00"),
                            ("11", "18:00 às 19:00"),
                            ("12", "19:00 às 20:00"),
                        ],
                        max_length=20,
                        verbose_name="Horário",
                    ),
                ),
            ],
            options={
                "verbose_name": "Reserva de sala de reunião",
                "verbose_name_plural": "Reservas de salas de reunião",
                "ordering": ("data", "horario", "sala_reuniao"),
            },
        ),
        migrations.CreateModel(
            name="ReservaTablet",
            fields=[
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
                (
                    "data",
                    models.DateField(
                        validators=[apps.utils.validators.DateValidator()],
                        verbose_name="Data",
                    ),
                ),
                (
                    "horario",
                    models.CharField(
                        choices=[
                            ("1", "08:00 às 09:00"),
                            ("2", "09:00 às 10:00"),
                            ("3", "10:00 às 11:00"),
                            ("4", "11:00 às 12:00"),
                            ("5", "12:00 às 13:00"),
                            ("6", "13:00 às 14:00"),
                            ("7", "14:00 às 15:00"),
                            ("8", "15:00 às 16:00"),
                            ("9", "16:00 às 17:00"),
                            ("10", "17:00 às 18:00"),
                            ("11", "18:00 às 19:00"),
                            ("12", "19:00 às 20:00"),
                        ],
                        max_length=20,
                        verbose_name="Horário",
                    ),
                ),
                (
                    "tablet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="reservas_tablets",
                        to="recursos.tablet",
                        verbose_name="Tablet",
                    ),
                ),
            ],
            options={
                "verbose_name": "Reserva de tablet",
                "verbose_name_plural": "Reservas de tablets",
                "ordering": ("data", "horario", "tablet"),
            },
        ),
    ]
