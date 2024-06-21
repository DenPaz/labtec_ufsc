from django.urls import path

from .views import (
    ReservaComputadorCreateView,
    ReservaComputadorDeleteView,
    ReservaComputadorListView,
    ReservaComputadorUpdateView,
)

app_name = "reservas"

urlpatterns = [
    path(
        route="reserva-computador-list/",
        view=ReservaComputadorListView.as_view(),
        name="reserva_computador_list",
    ),
    path(
        route="reserva-computador-create/",
        view=ReservaComputadorCreateView.as_view(),
        name="reserva_computador_create",
    ),
    path(
        route="reserva-computador-update/<uuid:pk>/",
        view=ReservaComputadorUpdateView.as_view(),
        name="reserva_computador_update",
    ),
    path(
        route="reserva-computador-delete/<uuid:pk>/",
        view=ReservaComputadorDeleteView.as_view(),
        name="reserva_computador_delete",
    ),
]
