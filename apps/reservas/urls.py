from django.urls import path

from .views import (
    ReservaComputadorCreateView,
    ReservaComputadorDeleteView,
    ReservaComputadorListView,
    ReservaComputadorUpdateView,
    ReservaKitTabletCreateView,
    ReservaKitTabletDeleteView,
    ReservaKitTabletListView,
    ReservaKitTabletUpdateView,
    ReservaMesaTrabalhoCreateView,
    ReservaMesaTrabalhoDeleteView,
    ReservaMesaTrabalhoListView,
    ReservaMesaTrabalhoUpdateView,
    ReservaOculusVRCreateView,
    ReservaOculusVRDeleteView,
    ReservaOculusVRListView,
    ReservaOculusVRUpdateView,
    ReservaSalaReuniaoCreateView,
    ReservaSalaReuniaoDeleteView,
    ReservaSalaReuniaoListView,
    ReservaSalaReuniaoUpdateView,
    ReservaTabletCreateView,
    ReservaTabletDeleteView,
    ReservaTabletListView,
    ReservaTabletUpdateView,
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
    path(
        route="reserva-tablet-list/",
        view=ReservaTabletListView.as_view(),
        name="reserva_tablet_list",
    ),
    path(
        route="reserva-tablet-create/",
        view=ReservaTabletCreateView.as_view(),
        name="reserva_tablet_create",
    ),
    path(
        route="reserva-tablet-update/<uuid:pk>/",
        view=ReservaTabletUpdateView.as_view(),
        name="reserva_tablet_update",
    ),
    path(
        route="reserva-tablet-delete/<uuid:pk>/",
        view=ReservaTabletDeleteView.as_view(),
        name="reserva_tablet_delete",
    ),
    path(
        route="reserva-kit-tablet-list/",
        view=ReservaKitTabletListView.as_view(),
        name="reserva_kit_tablet_list",
    ),
    path(
        route="reserva-kit-tablet-create/",
        view=ReservaKitTabletCreateView.as_view(),
        name="reserva_kit_tablet_create",
    ),
    path(
        route="reserva-kit-tablet-update/<uuid:pk>/",
        view=ReservaKitTabletUpdateView.as_view(),
        name="reserva_kit_tablet_update",
    ),
    path(
        route="reserva-kit-tablet-delete/<uuid:pk>/",
        view=ReservaKitTabletDeleteView.as_view(),
        name="reserva_kit_tablet_delete",
    ),
    path(
        route="reserva-oculus-vr-list/",
        view=ReservaOculusVRListView.as_view(),
        name="reserva_oculus_vr_list",
    ),
    path(
        route="reserva-oculus-vr-create/",
        view=ReservaOculusVRCreateView.as_view(),
        name="reserva_oculus_vr_create",
    ),
    path(
        route="reserva-oculus-vr-update/<uuid:pk>/",
        view=ReservaOculusVRUpdateView.as_view(),
        name="reserva_oculus_vr_update",
    ),
    path(
        route="reserva-oculus-vr-delete/<uuid:pk>/",
        view=ReservaOculusVRDeleteView.as_view(),
        name="reserva_oculus_vr_delete",
    ),
    path(
        route="reserva-mesa-trabalho-list/",
        view=ReservaMesaTrabalhoListView.as_view(),
        name="reserva_mesa_trabalho_list",
    ),
    path(
        route="reserva-mesa-trabalho-create/",
        view=ReservaMesaTrabalhoCreateView.as_view(),
        name="reserva_mesa_trabalho_create",
    ),
    path(
        route="reserva-mesa-trabalho-update/<uuid:pk>/",
        view=ReservaMesaTrabalhoUpdateView.as_view(),
        name="reserva_mesa_trabalho_update",
    ),
    path(
        route="reserva-mesa-trabalho-delete/<uuid:pk>/",
        view=ReservaMesaTrabalhoDeleteView.as_view(),
        name="reserva_mesa_trabalho_delete",
    ),
    path(
        route="reserva-sala-reuniao-list/",
        view=ReservaSalaReuniaoListView.as_view(),
        name="reserva_sala_reuniao_list",
    ),
    path(
        route="reserva-sala-reuniao-create/",
        view=ReservaSalaReuniaoCreateView.as_view(),
        name="reserva_sala_reuniao_create",
    ),
    path(
        route="reserva-sala-reuniao-update/<uuid:pk>/",
        view=ReservaSalaReuniaoUpdateView.as_view(),
        name="reserva_sala_reuniao_update",
    ),
    path(
        route="reserva-sala-reuniao-delete/<uuid:pk>/",
        view=ReservaSalaReuniaoDeleteView.as_view(),
        name="reserva_sala_reuniao_delete",
    ),
]
