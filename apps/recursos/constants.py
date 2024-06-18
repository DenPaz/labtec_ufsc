from django.db import models
from django.utils.translation import gettext_lazy as _


class SO(models.TextChoices):
    WINDOWS = "Windows", _("Windows")
    LINUX = "Linux", _("Linux")


class SOMobile(models.TextChoices):
    ANDROID = "Android", _("Android")
    IOS = "iOS", _("iOS")
