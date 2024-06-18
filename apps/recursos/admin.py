from django.contrib import admin

from .models import Computador, KitTablet, MesaTrabalho, OculusVR, SalaReuniao, Tablet


class RecursoAdmin(admin.ModelAdmin):
    list_display = ["id"]
    search_fields = list_display
    readonly_fields = ["created", "modified"]
    list_per_page = 10


@admin.register(Computador)
class ComputadorAdmin(RecursoAdmin):
    list_display = [
        "id",
        "processador",
        "memoria_ram",
        "placa_video",
        "armazenamento",
        "so_principal",
        "so_secundario",
        "fone_ouvido",
    ]


@admin.register(Tablet)
class TabletAdmin(RecursoAdmin):
    list_display = [
        "id",
        "modelo",
        "marca",
        "tamanho_tela",
        "so",
        "armazenamento",
    ]


@admin.register(KitTablet)
class KitTabletAdmin(RecursoAdmin):
    list_display = [
        "id",
        "tablet",
        "caneta",
        "teclado",
        "mouse",
    ]


@admin.register(OculusVR)
class OculusVRAdmin(RecursoAdmin):
    list_display = [
        "id",
        "modelo",
        "marca",
        "resolucao",
    ]


@admin.register(MesaTrabalho)
class MesaTrabalhoAdmin(RecursoAdmin):
    list_display = [
        "id",
        "monitor",
        "mouse_pad",
        "fone_ouvido",
    ]


@admin.register(SalaReuniao)
class SalaReuniaoAdmin(RecursoAdmin):
    list_display = [
        "id",
        "mesas",
        "cadeiras",
        "projetor",
        "quadro",
    ]
