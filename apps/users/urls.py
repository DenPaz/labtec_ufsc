from django.urls import path

from .views import UserDetailView, UserUpdateView

app_name = "users"

urlpatterns = [
    path(
        route="profile/<uuid:pk>/",
        view=UserDetailView.as_view(),
        name="user_detail",
    ),
    path(
        route="profile/<uuid:pk>/update/",
        view=UserUpdateView.as_view(),
        name="user_update",
    ),
]
