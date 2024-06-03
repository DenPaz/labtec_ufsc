from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("apps.dashboard.urls", namespace="dashboard")),
    path("users/", include("apps.users.urls", namespace="users")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path(
            route="400/",
            view=default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            route="403/",
            view=default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            route="404/",
            view=default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path(
            route="500/",
            view=default_views.server_error,
            kwargs={"exception": Exception("Internal Server Error")},
        ),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
