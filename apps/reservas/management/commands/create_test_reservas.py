from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from apps.recursos.models import (
    Computador,
    KitTablet,
    MesaTrabalho,
    OculusVR,
    SalaReuniao,
    Tablet,
)

from ...models import ReservaComputador

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        test_reservas_computadores = [
            {
                "user": 1,
                "data": "2024-06-12",
                "horario": 1,
                "computador": 1,
            },
            {
                "user": 1,
                "data": "2024-06-13",
                "horario": 1,
                "computador": 2,
            },
            {
                "user": 1,
                "data": "2024-06-16",
                "horario": 1,
                "computador": 1,
            },
            {
                "user": 1,
                "data": "2024-06-18",
                "horario": 1,
                "computador": 2,
            },
            {
                "user": 1,
                "data": "2024-06-20",
                "horario": 1,
                "computador": 2,
            },
        ]

        model_data = [
            (ReservaComputador, test_reservas_computadores),
        ]

        for model, data in model_data:
            for item in data:
                item["user"] = User.objects.get(pk=item["user"])
                item["computador"] = Computador.objects.get(numero=item.pop("computador"))
                model.objects.update_or_create(**item)
