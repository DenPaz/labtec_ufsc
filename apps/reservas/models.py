import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.recursos.models import Computador
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
        related_name="reservas",
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
        related_name="reservas",
        verbose_name=_("Computador"),
    )

    class Meta:
        verbose_name = _("Reserva de computador")
        verbose_name_plural = _("Reservas de computadores")
        unique_together = ("data", "horario", "computador")
        ordering = ("data", "horario", "computador")

    def __str__(self):
        return f"Reserva de {self.computador}: {super().__str__()}"
