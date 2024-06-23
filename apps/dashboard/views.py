from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from django.views.generic import TemplateView

from apps.recursos.models import (
    Computador,
    KitTablet,
    MesaTrabalho,
    OculusVR,
    SalaReuniao,
    Tablet,
)
from apps.reservas.models import (
    ReservaComputador,
    ReservaKitTablet,
    ReservaMesaTrabalho,
    ReservaOculusVR,
    ReservaSalaReuniao,
    ReservaTablet,
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


class ConsultasView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/consultas.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["consulta_1"] = self.get_consulta_1()
        context["consulta_2"] = self.get_consulta_2()
        context["consulta_3"] = self.get_consulta_3()
        return context

    # Consulta 1: Listar os usuários que fizeram reserva de computadores, com a quantidade de reservas feitas por cada um e o número do computador reservado.
    def get_consulta_1(self):
        consulta_1 = (
            User.objects.filter(
                reservacomputador__isnull=False,
            )
            .values(
                "first_name",
                "last_name",
                "reservacomputador__computador__numero",
            )
            .annotate(
                total_reservas=Count("reservacomputador"),
            )
            .order_by(
                "first_name",
                "last_name",
                "reservacomputador__computador__numero",
            )
        )
        return consulta_1

    # Consulta 2: Listar os usuários que fizeram uma reserva de uma sala de reunião que tem um projetor no mês de junho de 2024 com a quantidade de reservas feitas por cada um e o número da sala reservada.
    def get_consulta_2(self):
        consulta_2 = (
            User.objects.filter(
                reservasalareuniao__sala_reuniao__projetor=True,
                reservasalareuniao__data__year=2024,
                reservasalareuniao__data__month=6,
            )
            .values(
                "first_name",
                "last_name",
                "reservasalareuniao__sala_reuniao__numero",
            )
            .annotate(
                total_reservas=Count("reservasalareuniao"),
            )
            .order_by("first_name", "last_name")
        )
        return consulta_2

    # Consulta 3: Listar os usuários que fizeram reserva de mesa de trabalho ou kit tablet, com a quantidade de reservas feitas por cada um e o número da mesa de trabalho ou kit tablet reservado.
    def get_consulta_3(self):
        consulta_3 = (
            User.objects.filter(Q(reservamesatrabalho__isnull=False) | Q(reservakittablet__isnull=False))
            .values(
                "first_name",
                "last_name",
                "reservamesatrabalho__mesa_trabalho__numero",
                "reservakittablet__kit_tablet__numero",
            )
            .annotate(
                total_reservas_mesa=Count("reservamesatrabalho"),
                total_reservas_kit=Count("reservakittablet"),
            )
            .order_by("first_name", "last_name")
        )
        return consulta_3
