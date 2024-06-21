from django.db import models


class Horarios(models.TextChoices):
    HORARIO_08 = 1, "08:00 às 09:00"
    HORARIO_09 = 2, "09:00 às 10:00"
    HORARIO_10 = 3, "10:00 às 11:00"
    HORARIO_11 = 4, "11:00 às 12:00"
    HORARIO_12 = 5, "12:00 às 13:00"
    HORARIO_13 = 6, "13:00 às 14:00"
    HORARIO_14 = 7, "14:00 às 15:00"
    HORARIO_15 = 8, "15:00 às 16:00"
    HORARIO_16 = 9, "16:00 às 17:00"
    HORARIO_17 = 10, "17:00 às 18:00"
    HORARIO_18 = 11, "18:00 às 19:00"
    HORARIO_19 = 12, "19:00 às 20:00"
