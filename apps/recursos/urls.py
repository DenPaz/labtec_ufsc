from django.urls import path

from .views import ComputadorListView

app_name = "recursos"

urlpatterns = [
    path(
        route="computador-list/",
        view=ComputadorListView.as_view(),
        name="computador_list",
    ),
]
