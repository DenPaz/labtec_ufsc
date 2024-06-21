from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, View
from utils.viewmixins import SearchMixin, StaffuserRequiredMixin

from .forms import (
    ComputadorForm,
    KitTabletForm,
    MesaTrabalhoForm,
    OculusVRForm,
    SalaReuniaoForm,
    TabletForm,
)
from .models import Computador, KitTablet, MesaTrabalho, OculusVR, SalaReuniao, Tablet


class RecursoListView(LoginRequiredMixin, StaffuserRequiredMixin, SearchMixin, ListView):
    ordering = ["numero"]
    paginate_by = 5


class RecursoCreateView(LoginRequiredMixin, StaffuserRequiredMixin, SuccessMessageMixin, CreateView):
    pass


class RecursoUpdateView(LoginRequiredMixin, StaffuserRequiredMixin, SuccessMessageMixin, UpdateView):
    pass


class RecursoDeleteView(LoginRequiredMixin, StaffuserRequiredMixin, View):
    model = None
    success_url = None

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=kwargs["pk"])
        obj.delete()
        messages.success(request, self.get_success_message())
        return redirect(self.get_success_url())

    def get_success_url(self):
        return self.success_url

    def get_success_message(self):
        return f"{self.model._meta.verbose_name} deletado com sucesso."


class ComputadorListView(RecursoListView):
    model = Computador
    search_fields = [
        "numero",
        "processador",
        "placa_video",
        "so_principal",
    ]
    template_name = "recursos/computador/computador_list.html"


class ComputadorCreateView(RecursoCreateView):
    model = Computador
    form_class = ComputadorForm
    success_url = reverse_lazy("recursos:computador_list")
    success_message = "Computador criado com sucesso."
    template_name = "recursos/computador/computador_create.html"


class ComputadorUpdateView(RecursoUpdateView):
    model = Computador
    form_class = ComputadorForm
    success_url = reverse_lazy("recursos:computador_list")
    success_message = "Computador atualizado com sucesso."
    template_name = "recursos/computador/computador_update.html"


class ComputadorDeleteView(RecursoDeleteView):
    model = Computador
    success_url = reverse_lazy("recursos:computador_list")


class TabletListView(RecursoListView):
    model = Tablet
    search_fields = [
        "numero",
        "modelo",
        "marca",
        "so",
    ]
    template_name = "recursos/tablet/tablet_list.html"


class TabletCreateView(RecursoCreateView):
    model = Tablet
    form_class = TabletForm
    success_url = reverse_lazy("recursos:tablet_list")
    success_message = "Tablet criado com sucesso."
    template_name = "recursos/tablet/tablet_create.html"


class TabletUpdateView(RecursoUpdateView):
    model = Tablet
    form_class = TabletForm
    success_url = reverse_lazy("recursos:tablet_list")
    success_message = "Tablet atualizado com sucesso."
    template_name = "recursos/tablet/tablet_update.html"


class TabletDeleteView(RecursoDeleteView):
    model = Tablet
    success_url = reverse_lazy("recursos:tablet_list")
