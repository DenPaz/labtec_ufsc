from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, View

from .forms import (
    ReservaComputadorForm,
    ReservaKitTabletForm,
    ReservaMesaTrabalhoForm,
    ReservaOculusVRForm,
    ReservaSalaReuniaoForm,
    ReservaTabletForm,
)
from .models import (
    ReservaComputador,
    ReservaKitTablet,
    ReservaMesaTrabalho,
    ReservaOculusVR,
    ReservaSalaReuniao,
    ReservaTablet,
)


class ReservaListView(LoginRequiredMixin, ListView):
    ordering = ["data", "horario"]
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ReservaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReservaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ReservaDeleteView(LoginRequiredMixin, View):
    model = None
    success_url = None

    def post(self, request, *args, **kwargs):
        reserva = get_object_or_404(self.model, user=request.user, pk=kwargs["pk"])
        reserva.delete()
        messages.success(request, "Reserva cancelada com sucesso.")
        return redirect(self.success_url)

    def get_success_url(self):
        return self.success_url

    def get_success_message(self):
        return f"{self.model._meta.verbose_name} deletada com sucesso."


class ReservaComputadorListView(ReservaListView):
    model = ReservaComputador
    template_name = "reservas/reserva_computador/list.html"


class ReservaComputadorCreateView(ReservaCreateView):
    model = ReservaComputador
    form_class = ReservaComputadorForm
    template_name = "reservas/reserva_computador/create.html"
    success_url = reverse_lazy("reservas:reserva_computador_list")
    success_message = "Reserva de computador feita com sucesso."


class ReservaComputadorUpdateView(ReservaUpdateView):
    model = ReservaComputador
    form_class = ReservaComputadorForm
    template_name = "reservas/reserva_computador/update.html"
    success_url = reverse_lazy("reservas:reserva_computador_list")
    success_message = "Reserva de computador atualizada com sucesso."


class ReservaComputadorDeleteView(ReservaDeleteView):
    model = ReservaComputador
    success_url = reverse_lazy("reservas:reserva_computador_list")


class ReservaTabletListView(ReservaListView):
    model = ReservaTablet
    template_name = "reservas/reserva_tablet/list.html"


class ReservaTabletCreateView(ReservaCreateView):
    model = ReservaTablet
    form_class = ReservaTabletForm
    template_name = "reservas/reserva_tablet/create.html"
    success_url = reverse_lazy("reservas:reserva_tablet_list")
    success_message = "Reserva de tablet feita com sucesso."


class ReservaTabletUpdateView(ReservaUpdateView):
    model = ReservaTablet
    form_class = ReservaTabletForm
    template_name = "reservas/reserva_tablet/update.html"
    success_url = reverse_lazy("reservas:reserva_tablet_list")
    success_message = "Reserva de tablet atualizada com sucesso."


class ReservaTabletDeleteView(ReservaDeleteView):
    model = ReservaTablet
    success_url = reverse_lazy("reservas:reserva_tablet_list")


class ReservaKitTabletListView(ReservaListView):
    model = ReservaKitTablet
    template_name = "reservas/reserva_kit_tablet/list.html"


class ReservaKitTabletCreateView(ReservaCreateView):
    model = ReservaKitTablet
    form_class = ReservaKitTabletForm
    template_name = "reservas/reserva_kit_tablet/create.html"
    success_url = reverse_lazy("reservas:reserva_kit_tablet_list")
    success_message = "Reserva de kit tablet feita com sucesso."


class ReservaKitTabletUpdateView(ReservaUpdateView):
    model = ReservaKitTablet
    form_class = ReservaKitTabletForm
    template_name = "reservas/reserva_kit_tablet/update.html"
    success_url = reverse_lazy("reservas:reserva_kit_tablet_list")
    success_message = "Reserva de kit tablet atualizada com sucesso."


class ReservaKitTabletDeleteView(ReservaDeleteView):
    model = ReservaKitTablet
    success_url = reverse_lazy("reservas:reserva_kit_tablet_list")


class ReservaOculusVRListView(ReservaListView):
    model = ReservaOculusVR
    template_name = "reservas/reserva_oculus_vr/list.html"


class ReservaOculusVRCreateView(ReservaCreateView):
    model = ReservaOculusVR
    form_class = ReservaOculusVRForm
    template_name = "reservas/reserva_oculus_vr/create.html"
    success_url = reverse_lazy("reservas:reserva_oculus_vr_list")
    success_message = "Reserva de Oculus VR feita com sucesso."


class ReservaOculusVRUpdateView(ReservaUpdateView):
    model = ReservaOculusVR
    form_class = ReservaOculusVRForm
    template_name = "reservas/reserva_oculus_vr/update.html"
    success_url = reverse_lazy("reservas:reserva_oculus_vr_list")
    success_message = "Reserva de Oculus VR atualizada com sucesso."


class ReservaOculusVRDeleteView(ReservaDeleteView):
    model = ReservaOculusVR
    success_url = reverse_lazy("reservas:reserva_oculus_vr_list")


class ReservaMesaTrabalhoListView(ReservaListView):
    model = ReservaMesaTrabalho
    template_name = "reservas/reserva_mesa_trabalho/list.html"


class ReservaMesaTrabalhoCreateView(ReservaCreateView):
    model = ReservaMesaTrabalho
    form_class = ReservaMesaTrabalhoForm
    template_name = "reservas/reserva_mesa_trabalho/create.html"
    success_url = reverse_lazy("reservas:reserva_mesa_trabalho_list")
    success_message = "Reserva de mesa de trabalho feita com sucesso."


class ReservaMesaTrabalhoUpdateView(ReservaUpdateView):
    model = ReservaMesaTrabalho
    form_class = ReservaMesaTrabalhoForm
    template_name = "reservas/reserva_mesa_trabalho/update.html"
    success_url = reverse_lazy("reservas:reserva_mesa_trabalho_list")
    success_message = "Reserva de mesa de trabalho atualizada com sucesso."


class ReservaMesaTrabalhoDeleteView(ReservaDeleteView):
    model = ReservaMesaTrabalho
    success_url = reverse_lazy("reservas:reserva_mesa_trabalho_list")


class ReservaSalaReuniaoListView(ReservaListView):
    model = ReservaSalaReuniao
    template_name = "reservas/reserva_sala_reuniao/list.html"


class ReservaSalaReuniaoCreateView(ReservaCreateView):
    model = ReservaSalaReuniao
    form_class = ReservaSalaReuniaoForm
    template_name = "reservas/reserva_sala_reuniao/create.html"
    success_url = reverse_lazy("reservas:reserva_sala_reuniao_list")
    success_message = "Reserva de sala de reunião feita com sucesso."


class ReservaSalaReuniaoUpdateView(ReservaUpdateView):
    model = ReservaSalaReuniao
    form_class = ReservaSalaReuniaoForm
    template_name = "reservas/reserva_sala_reuniao/update.html"
    success_url = reverse_lazy("reservas:reserva_sala_reuniao_list")
    success_message = "Reserva de sala de reunião atualizada com sucesso."


class ReservaSalaReuniaoDeleteView(ReservaDeleteView):
    model = ReservaSalaReuniao
    success_url = reverse_lazy("reservas:reserva_sala_reuniao_list")
