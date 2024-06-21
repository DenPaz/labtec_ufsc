from django.urls import path

from .views import (
    ComputadorCreateView,
    ComputadorDeleteView,
    ComputadorListView,
    ComputadorUpdateView,
    TabletCreateView,
    TabletDeleteView,
    TabletListView,
    TabletUpdateView,
)

app_name = "recursos"

urlpatterns = [
    path(
        route="computador-list/",
        view=ComputadorListView.as_view(),
        name="computador_list",
    ),
    path(
        route="computador-create/",
        view=ComputadorCreateView.as_view(),
        name="computador_create",
    ),
    path(
        route="computador-update/<uuid:pk>/",
        view=ComputadorUpdateView.as_view(),
        name="computador_update",
    ),
    path(
        route="computador-delete/<uuid:pk>/",
        view=ComputadorDeleteView.as_view(),
        name="computador_delete",
    ),
    path(
        route="tablet-list/",
        view=TabletListView.as_view(),
        name="tablet_list",
    ),
    path(
        route="tablet-create/",
        view=TabletCreateView.as_view(),
        name="tablet_create",
    ),
    path(
        route="tablet-update/<uuid:pk>/",
        view=TabletUpdateView.as_view(),
        name="tablet_update",
    ),
    path(
        route="tablet-delete/<uuid:pk>/",
        view=TabletDeleteView.as_view(),
        name="tablet_delete",
    ),
]
