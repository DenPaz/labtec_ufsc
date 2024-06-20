from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View
from utils.viewmixins import SearchMixin, StaffuserRequiredMixin

from .models import Computador, KitTablet, MesaTrabalho, OculusVR, SalaReuniao, Tablet


class RecursoListView(LoginRequiredMixin, StaffuserRequiredMixin, SearchMixin, ListView):
    ordering = ["id"]
    paginate_by = 8


class RecursoCreateView(LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class RecursoDeleteView(LoginRequiredMixin, StaffuserRequiredMixin, View):
    model = None
    success_url = None

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=kwargs["pk"])
        obj.delete()
        messages.success(request, self.get_success_message())
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)

    def get_success_message(self):
        return f"{self.model._meta.verbose_name} deletado com sucesso."


class ComputadorListView(RecursoListView):
    model = Computador
    search_fields = [
        "id",
        "processador",
        "placa_video",
        "so_principal",
        "so_secundario",
    ]
    template_name = "recursos/computador_list.html"


class ComputadorCreateView(RecursoCreateView):
    model = Computador
    template_name = "recursos/computador_create.html"
    success_url = "recursos:computador_list"


class ComputadorDeleteView(RecursoDeleteView):
    model = Computador
    success_url = "recursos:computador_list"
