from django.db import models
from django.utils.translation import gettext_lazy as _


class Cursos(models.TextChoices):
    EC = "EC", _("Engenharia de Computação")
    EE = "EE", _("Engenharia de Energia")
    FISIO = "FISIO", _("Fisioterapia")
    MED = "MED", _("Medicina")
    TIC = "TIC", _("Tecnologias da Informação e Comunicação")
