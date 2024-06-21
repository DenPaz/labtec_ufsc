import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.recursos.models import (
    Computador,
    KitTablet,
    MesaTrabalho,
    OculusVR,
    SalaReuniao,
    Tablet,
)
from apps.utils.validators import DateValidator

from .constants import Horarios

User = get_user_model()


class Reserva(models.Model):
    id = models.UUIDField(
        verbose_name=_("ID"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        verbose_name=_("Usuário"),
    )
    data = models.DateField(
        verbose_name=_("Data"),
        validators=[DateValidator()],
    )
    horario = models.CharField(
        verbose_name=_("Horário"),
        choices=Horarios.choices,
        max_length=20,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.user.get_full_name()}, {self.data}, {self.get_horario_display()}"


class ReservaComputador(Reserva):
    computador = models.ForeignKey(
        to=Computador,
        on_delete=models.PROTECT,
        related_name="reservas_computadores",
        verbose_name=_("Computador"),
    )

    class Meta:
        verbose_name = _("Reserva de computador")
        verbose_name_plural = _("Reservas de computadores")
        unique_together = ("data", "horario", "computador")
        ordering = ("data", "horario", "computador")

    def __str__(self):
        return f"Reserva de {self.computador}: {super().__str__()}"


class ReservaTablet(Reserva):
    tablet = models.ForeignKey(
        to=Tablet,
        on_delete=models.PROTECT,
        related_name="reservas_tablets",
        verbose_name=_("Tablet"),
    )

    class Meta:
        verbose_name = _("Reserva de tablet")
        verbose_name_plural = _("Reservas de tablets")
        unique_together = ("data", "horario", "tablet")
        ordering = ("data", "horario", "tablet")

    def __str__(self):
        return f"Reserva de {self.tablet}: {super().__str__()}"


class ReservaKitTablet(Reserva):
    kit_tablet = models.ForeignKey(
        to=KitTablet,
        on_delete=models.PROTECT,
        related_name="reservas_kits_tablet",
        verbose_name=_("Kit de tablet"),
    )

    class Meta:
        verbose_name = _("Reserva de kit de tablet")
        verbose_name_plural = _("Reservas de kits de tablet")
        unique_together = ("data", "horario", "kit_tablet")
        ordering = ("data", "horario", "kit_tablet")

    def __str__(self):
        return f"Reserva de {self.kit_tablet}: {super().__str__()}"


class ReservaOculusVR(Reserva):
    oculus_vr = models.ForeignKey(
        to=OculusVR,
        on_delete=models.PROTECT,
        related_name="reservas_oculus_vr",
        verbose_name=_("Oculus VR"),
    )

    class Meta:
        verbose_name = _("Reserva de Oculus VR")
        verbose_name_plural = _("Reservas de Oculus VR")
        unique_together = ("data", "horario", "oculus_vr")
        ordering = ("data", "horario", "oculus_vr")

    def __str__(self):
        return f"Reserva de {self.oculus_vr}: {super().__str__()}"


class ReservaMesaTrabalho(Reserva):
    mesa_trabalho = models.ForeignKey(
        to=MesaTrabalho,
        on_delete=models.PROTECT,
        related_name="reservas_mesas_trabalho",
        verbose_name=_("Mesa de trabalho"),
    )

    class Meta:
        verbose_name = _("Reserva de mesa de trabalho")
        verbose_name_plural = _("Reservas de mesas de trabalho")
        unique_together = ("data", "horario", "mesa_trabalho")
        ordering = ("data", "horario", "mesa_trabalho")

    def __str__(self):
        return f"Reserva de {self.mesa_trabalho}: {super().__str__()}"


class ReservaSalaReuniao(Reserva):
    sala_reuniao = models.ForeignKey(
        to=SalaReuniao,
        on_delete=models.PROTECT,
        related_name="reservas_salas_reuniao",
        verbose_name=_("Sala de reunião"),
    )

    class Meta:
        verbose_name = _("Reserva de sala de reunião")
        verbose_name_plural = _("Reservas de salas de reunião")
        unique_together = ("data", "horario", "sala_reuniao")
        ordering = ("data", "horario", "sala_reuniao")

    def __str__(self):
        return f"Reserva de {self.sala_reuniao}: {super().__str__()}"
