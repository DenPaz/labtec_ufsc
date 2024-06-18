from django.shortcuts import render
from django.views.generic import ListView

from .models import Computador, KitTablet, MesaTrabalho, OculusVR, SalaReuniao, Tablet


class RecursoListView(ListView):
    ordering = ["id"]
    paginate_by = 10


class ComputadorListView(RecursoListView):
    model = Computador
    template_name = "recursos/computador_list.html"
