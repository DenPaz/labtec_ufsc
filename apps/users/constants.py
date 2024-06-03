from django.db import models
from django.utils.translation import gettext_lazy as _


class Cursos(models.TextChoices):
    EC = "Engenharia de Computação", _("Engenharia de Computação")
    EE = "Engenharia de Energia", _("Engenharia de Energia")
    FISIO = "Fisioterapia", _("Fisioterapia")
    MED = "Medicina", _("Medicina")
    TICT = "Tecnologias da Informação e Comunicação", _("Tecnologias da Informação e Comunicação")
