from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "apps.users"
    verbose_name = _("Usuários")

    def ready(self):
        import apps.users.signals
