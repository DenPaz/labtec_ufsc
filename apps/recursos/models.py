from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from .constants import SO, SOMobile


class Recurso(TimeStampedModel):
    id = models.PositiveIntegerField(
        verbose_name=_("ID"),
        primary_key=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self._meta.verbose_name}-{self.id}"

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Computador(Recurso):
    processador = models.CharField(
        verbose_name=_("Processador"),
        max_length=100,
    )
    memoria_ram = models.PositiveIntegerField(
        verbose_name=_("Memória RAM (GB)"),
    )
    placa_video = models.CharField(
        verbose_name=_("Placa de vídeo"),
        max_length=100,
    )
    armazenamento = models.PositiveIntegerField(
        verbose_name=_("Armazenamento"),
    )
    so_principal = models.CharField(
        verbose_name=_("SO. principal"),
        choices=SO.choices,
        max_length=10,
    )
    so_secundario = models.CharField(
        verbose_name=_("SO. secundário"),
        choices=SO.choices,
        max_length=10,
        blank=True,
    )
    fone_ouvido = models.BooleanField(
        verbose_name=_("Inclui fone de ouvido?"),
        default=True,
    )
    danificado = models.BooleanField(
        verbose_name=_("Esta danificado?"),
        default=False,
    )

    class Meta:
        verbose_name = _("Computador")
        verbose_name_plural = _("Computadores")
        ordering = ["id"]


class Tablet(Recurso):
    modelo = models.CharField(
        verbose_name=_("Modelo"),
        max_length=100,
    )
    marca = models.CharField(
        verbose_name=_("Marca"),
        max_length=100,
    )
    tamanho_tela = models.FloatField(
        verbose_name=_("Tamanho da tela"),
    )
    so = models.CharField(
        verbose_name=_("Sist. Operacional"),
        choices=SOMobile.choices,
        max_length=10,
    )
    armazenamento = models.PositiveIntegerField(
        verbose_name=_("Armazenamento"),
    )
    danificado = models.BooleanField(
        verbose_name=_("Esta danificado?"),
        default=False,
    )

    class Meta:
        verbose_name = _("Tablet")
        verbose_name_plural = _("Tablets")
        ordering = ["id"]


class KitTablet(Recurso):
    tablet = models.OneToOneField(
        to=Tablet,
        on_delete=models.PROTECT,
        related_name="kit",
        verbose_name=_("Tablet"),
    )
    caneta = models.BooleanField(
        verbose_name=_("Possui caneta?"),
        default=True,
    )
    teclado = models.BooleanField(
        verbose_name=_("Possui teclado?"),
        default=True,
    )
    mouse = models.BooleanField(
        verbose_name=_(f"Possui mouse?"),
        default=True,
    )
    danificado = models.BooleanField(
        verbose_name=_("Esta danificado?"),
        default=False,
    )

    class Meta:
        verbose_name = _("Kit Tablet")
        verbose_name_plural = _("Kits Tablet")
        ordering = ["id"]


class OculusVR(Recurso):
    modelo = models.CharField(
        verbose_name=_("Modelo"),
        max_length=100,
    )
    marca = models.CharField(
        verbose_name=_("Marca"),
        max_length=100,
    )
    resolucao = models.CharField(
        verbose_name=_("Resolução"),
        max_length=100,
    )
    danificado = models.BooleanField(
        verbose_name=_("Esta danificado?"),
        default=False,
    )

    class Meta:
        verbose_name = _("Oculus VR")
        verbose_name_plural = _("Oculus VR")
        ordering = ["id"]


class MesaTrabalho(Recurso):
    monitor = models.BooleanField(
        verbose_name=_("Monitor"),
        default=True,
    )
    mouse_pad = models.BooleanField(
        verbose_name=_("Possui mouse pad?"),
        default=True,
    )
    fone_ouvido = models.BooleanField(
        verbose_name=_("Possui fone de ouvido?"),
        default=True,
    )

    class Meta:
        verbose_name = _("Mesa de trabalho")
        verbose_name_plural = _("Mesas de trabalho")
        ordering = ["id"]


class SalaReuniao(Recurso):
    mesas = models.PositiveIntegerField(
        verbose_name=_("Número de mesas"),
    )
    cadeiras = models.PositiveIntegerField(
        verbose_name=_("Número de cadeiras"),
    )
    projetor = models.BooleanField(
        verbose_name=_("Possui projetor?"),
        default=True,
    )
    quadro = models.BooleanField(
        verbose_name=_("Possui quadro?"),
        default=True,
    )

    class Meta:
        verbose_name = _("Sala de reunião")
        verbose_name_plural = _("Salas de reunião")
        ordering = ["id"]
