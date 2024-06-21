from django.urls import path

from .views import (
    ComputadorCreateView,
    ComputadorDeleteView,
    ComputadorListView,
    ComputadorUpdateView,
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
        route="computador-update/<int:pk>/",
        view=ComputadorUpdateView.as_view(),
        name="computador_update",
    ),
    path(
        route="computador-delete/<int:pk>/",
        view=ComputadorDeleteView.as_view(),
        name="computador_delete",
    ),
]
