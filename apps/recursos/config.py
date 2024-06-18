from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RecursosConfig(AppConfig):
    name = "apps.recursos"
    verbose_name = _("Recursos")

    def ready(self):
        import apps.recursos.signals
