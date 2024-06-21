from datetime import date

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, View

from .forms import ReservaComputadorForm
from .models import ReservaComputador


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
