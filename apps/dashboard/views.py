from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import TemplateView

from apps.recursos.models import (
    Computador,
    KitTablet,
    MesaTrabalho,
    OculusVR,
    SalaReuniao,
    Tablet,
)

User = get_user_model()


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reservas_computadores = (
            Computador.objects.annotate(
                total_reservas=Count(
                    "reservas_computadores",
                )
            )
            .values(
                "numero",
                "total_reservas",
            )
            .order_by("numero")
        )
        reservas_tablets = (
            Tablet.objects.annotate(
                total_reservas=Count(
                    "reservas_tablets",
                )
            )
            .values(
                "numero",
                "total_reservas",
            )
            .order_by("numero")
        )
        reservas_kits_tablets = (
            KitTablet.objects.annotate(
                total_reservas=Count(
                    "reservas_kits_tablet",
                )
            )
            .values(
                "numero",
                "total_reservas",
            )
            .order_by("numero")
        )
        reservas_oculus_vr = (
            OculusVR.objects.annotate(
                total_reservas=Count(
                    "reservas_oculus_vr",
                )
            )
            .values(
                "numero",
                "total_reservas",
            )
            .order_by("numero")
        )
        reservas_mesas_trabalho = (
            MesaTrabalho.objects.annotate(
                total_reservas=Count(
                    "reservas_mesas_trabalho",
                )
            )
            .values(
                "numero",
                "total_reservas",
            )
            .order_by("numero")
        )
        reservas_salas_reuniao = (
            SalaReuniao.objects.annotate(
                total_reservas=Count(
                    "reservas_salas_reuniao",
                )
            )
            .values(
                "numero",
                "total_reservas",
            )
            .order_by("numero")
        )
        context["reservas_computadores"] = reservas_computadores
        context["reservas_tablets"] = reservas_tablets
        context["reservas_kits_tablets"] = reservas_kits_tablets
        context["reservas_oculus_vr"] = reservas_oculus_vr
        context["reservas_mesas_trabalho"] = reservas_mesas_trabalho
        context["reservas_salas_reuniao"] = reservas_salas_reuniao

        return context
