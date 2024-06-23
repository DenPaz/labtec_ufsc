from django.urls import path

from .views import ConsultasView, IndexView

app_name = "dashboard"

urlpatterns = [
    path(
        route="",
        view=IndexView.as_view(),
        name="index",
    ),
    path(
        route="consultas/",
        view=ConsultasView.as_view(),
        name="consultas",
    ),
]
