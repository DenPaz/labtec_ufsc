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

from ...models import (
    ReservaComputador,
    ReservaKitTablet,
    ReservaMesaTrabalho,
    ReservaOculusVR,
    ReservaSalaReuniao,
    ReservaTablet,
)

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
            {
                "user": 2,
                "data": "2024-05-11",
                "horario": 3,
                "computador": 3,
            },
            {
                "user": 2,
                "data": "2024-02-02",
                "horario": 2,
                "computador": 2,
            },
            {
                "user": 2,
                "data": "2024-03-03",
                "horario": 1,
                "computador": 2,
            },
            {
                "user": 2,
                "data": "2024-06-22",
                "horario": 5,
                "computador": 3,
            },
            {
                "user": 2,
                "data": "2024-06-11",
                "horario": 4,
                "computador": 3,
            },
            {
                "user": 3,
                "data": "2024-03-11",
                "horario": 3,
                "computador": 6,
            },
            {
                "user": 3,
                "data": "2024-02-02",
                "horario": 2,
                "computador": 4,
            },
            {
                "user": 3,
                "data": "2024-03-03",
                "horario": 1,
                "computador": 7,
            },
            {
                "user": 3,
                "data": "2024-06-22",
                "horario": 5,
                "computador": 4,
            },
            {
                "user": 3,
                "data": "2024-06-11",
                "horario": 4,
                "computador": 5,
            },
            {
                "user": 4,
                "data": "2024-02-03",
                "horario": 3,
                "computador": 6,
            },
            {
                "user": 4,
                "data": "2024-06-11",
                "horario": 2,
                "computador": 4,
            },
            {
                "user": 4,
                "data": "2024-04-12",
                "horario": 7,
                "computador": 7,
            },
            {
                "user": 4,
                "data": "2024-06-13",
                "horario": 6,
                "computador": 4,
            },
            {
                "user": 4,
                "data": "2024-06-14",
                "horario": 5,
                "computador": 5,
            },
            {
                "user": 5,
                "data": "2024-02-03",
                "horario": 9,
                "computador": 8,
            },
            {
                "user": 5,
                "data": "2024-06-11",
                "horario": 3,
                "computador": 8,
            },
            {
                "user": 5,
                "data": "2024-04-12",
                "horario": 8,
                "computador": 9,
            },
            {
                "user": 5,
                "data": "2024-06-13",
                "horario": 4,
                "computador": 10,
            },
            {
                "user": 5,
                "data": "2024-06-21",
                "horario": 2,
                "computador": 10,
            },
            {
                "user": 6,
                "data": "2024-02-13",
                "horario": 3,
                "computador": 10,
            },
            {
                "user": 6,
                "data": "2024-06-11",
                "horario": 7,
                "computador": 9,
            },
            {
                "user": 6,
                "data": "2024-04-22",
                "horario": 6,
                "computador": 6,
            },
            {
                "user": 6,
                "data": "2024-06-23",
                "horario": 2,
                "computador": 7,
            },
            {
                "user": 6,
                "data": "2024-06-10",
                "horario": 1,
                "computador": 8,
            },
        ]
        test_reservas_tablets = [
            {
                "user": 1,
                "data": "2024-06-12",
                "horario": 1,
                "tablet": 1,
            },
            {
                "user": 1,
                "data": "2024-06-13",
                "horario": 1,
                "tablet": 2,
            },
            {
                "user": 1,
                "data": "2024-06-16",
                "horario": 1,
                "tablet": 1,
            },
            {
                "user": 1,
                "data": "2024-06-18",
                "horario": 1,
                "tablet": 2,
            },
            {
                "user": 1,
                "data": "2024-06-20",
                "horario": 1,
                "tablet": 2,
            },
            {
                "user": 2,
                "data": "2024-05-11",
                "horario": 3,
                "tablet": 3,
            },
            {
                "user": 2,
                "data": "2024-02-02",
                "horario": 2,
                "tablet": 2,
            },
            {
                "user": 2,
                "data": "2024-03-03",
                "horario": 1,
                "tablet": 2,
            },
            {
                "user": 2,
                "data": "2024-06-22",
                "horario": 5,
                "tablet": 3,
            },
            {
                "user": 2,
                "data": "2024-06-11",
                "horario": 4,
                "tablet": 3,
            },
            {
                "user": 3,
                "data": "2024-01-11",
                "horario": 3,
                "tablet": 2,
            },
            {
                "user": 3,
                "data": "2024-02-02",
                "horario": 2,
                "tablet": 4,
            },
            {
                "user": 3,
                "data": "2024-03-03",
                "horario": 1,
                "tablet": 3,
            },
            {
                "user": 3,
                "data": "2024-06-22",
                "horario": 5,
                "tablet": 4,
            },
            {
                "user": 3,
                "data": "2024-06-11",
                "horario": 4,
                "tablet": 5,
            },
            {
                "user": 4,
                "data": "2024-02-03",
                "horario": 3,
                "tablet": 2,
            },
            {
                "user": 4,
                "data": "2024-06-11",
                "horario": 2,
                "tablet": 1,
            },
            {
                "user": 4,
                "data": "2024-04-12",
                "horario": 7,
                "tablet": 3,
            },
            {
                "user": 4,
                "data": "2024-06-13",
                "horario": 6,
                "tablet": 4,
            },
            {
                "user": 4,
                "data": "2024-06-14",
                "horario": 5,
                "tablet": 5,
            },
            {
                "user": 5,
                "data": "2024-02-03",
                "horario": 9,
                "tablet": 2,
            },
            {
                "user": 5,
                "data": "2024-06-11",
                "horario": 3,
                "tablet": 5,
            },
            {
                "user": 5,
                "data": "2024-04-12",
                "horario": 8,
                "tablet": 5,
            },
            {
                "user": 5,
                "data": "2024-06-13",
                "horario": 4,
                "tablet": 2,
            },
            {
                "user": 5,
                "data": "2024-06-21",
                "horario": 2,
                "tablet": 3,
            },
            {
                "user": 6,
                "data": "2024-02-13",
                "horario": 3,
                "tablet": 1,
            },
            {
                "user": 6,
                "data": "2024-06-11",
                "horario": 7,
                "tablet": 1,
            },
            {
                "user": 6,
                "data": "2024-04-22",
                "horario": 6,
                "tablet": 3,
            },
            {
                "user": 6,
                "data": "2024-06-23",
                "horario": 2,
                "tablet": 2,
            },
            {
                "user": 6,
                "data": "2024-06-10",
                "horario": 1,
                "tablet": 4,
            },
        ]
        test_reservas_kits_tablets = [
            {
                "user": 1,
                "data": "2024-06-12",
                "horario": 1,
                "kit_tablet": 1,
            },
            {
                "user": 1,
                "data": "2024-06-13",
                "horario": 1,
                "kit_tablet": 2,
            },
            {
                "user": 1,
                "data": "2024-06-16",
                "horario": 1,
                "kit_tablet": 1,
            },
            {
                "user": 1,
                "data": "2024-06-18",
                "horario": 1,
                "kit_tablet": 2,
            },
            {
                "user": 1,
                "data": "2024-06-20",
                "horario": 1,
                "kit_tablet": 2,
            },
            {
                "user": 2,
                "data": "2024-02-02",
                "horario": 2,
                "kit_tablet": 1,
            },
            {
                "user": 2,
                "data": "2024-03-03",
                "horario": 1,
                "kit_tablet": 2,
            },
            {
                "user": 2,
                "data": "2024-06-22",
                "horario": 5,
                "kit_tablet": 2,
            },
            {
                "user": 2,
                "data": "2024-06-11",
                "horario": 4,
                "kit_tablet": 1,
            },
            {
                "user": 3,
                "data": "2024-06-22",
                "horario": 3,
                "kit_tablet": 1,
            },
            {
                "user": 3,
                "data": "2024-03-03",
                "horario": 1,
                "kit_tablet": 1,
            },
            {
                "user": 3,
                "data": "2024-06-22",
                "horario": 5,
                "kit_tablet": 1,
            },
            {
                "user": 3,
                "data": "2024-06-11",
                "horario": 4,
                "kit_tablet": 2,
            },
            {
                "user": 4,
                "data": "2024-02-03",
                "horario": 3,
                "kit_tablet": 2,
            },
            {
                "user": 4,
                "data": "2024-06-11",
                "horario": 2,
                "kit_tablet": 1,
            },
            {
                "user": 4,
                "data": "2024-04-12",
                "horario": 7,
                "kit_tablet": 2,
            },
            {
                "user": 4,
                "data": "2024-06-13",
                "horario": 6,
                "kit_tablet": 1,
            },
            {
                "user": 4,
                "data": "2024-06-14",
                "horario": 5,
                "kit_tablet": 2,
            },
            {
                "user": 5,
                "data": "2024-02-03",
                "horario": 9,
                "kit_tablet": 2,
            },
            {
                "user": 5,
                "data": "2024-06-11",
                "horario": 3,
                "kit_tablet": 2,
            },
            {
                "user": 5,
                "data": "2024-04-12",
                "horario": 8,
                "kit_tablet": 2,
            },
            {
                "user": 6,
                "data": "2024-06-23",
                "horario": 2,
                "kit_tablet": 2,
            },
            {
                "user": 6,
                "data": "2024-06-10",
                "horario": 1,
                "kit_tablet": 1,
            },
        ]
        test_reservas_oculus_vr = [
            {
                "user": 1,
                "data": "2024-06-12",
                "horario": 1,
                "oculus_vr": 1,
            },
            {
                "user": 2,
                "data": "2024-06-13",
                "horario": 1,
                "oculus_vr": 2,
            },
            {
                "user": 3,
                "data": "2024-06-16",
                "horario": 1,
                "oculus_vr": 3,
            },
            {
                "user": 4,
                "data": "2024-06-18",
                "horario": 1,
                "oculus_vr": 2,
            },
        ]
        test_reservas_mesa_trabalho = [
            {
                "user": 1,
                "data": "2024-06-12",
                "horario": 1,
                "mesa_trabalho": 1,
            },
            {
                "user": 2,
                "data": "2024-06-13",
                "horario": 1,
                "mesa_trabalho": 6,
            },
            {
                "user": 3,
                "data": "2024-06-16",
                "horario": 1,
                "mesa_trabalho": 7,
            },
            {
                "user": 4,
                "data": "2024-06-18",
                "horario": 1,
                "mesa_trabalho": 2,
            },
            {
                "user": 5,
                "data": "2024-04-12",
                "horario": 8,
                "mesa_trabalho": 9,
            },
            {
                "user": 5,
                "data": "2024-06-13",
                "horario": 4,
                "mesa_trabalho": 3,
            },
            {
                "user": 5,
                "data": "2024-06-21",
                "horario": 2,
                "mesa_trabalho": 3,
            },
            {
                "user": 6,
                "data": "2024-02-13",
                "horario": 3,
                "mesa_trabalho": 3,
            },
        ]
        test_reservas_sala_reuniao = [
            {
                "user": 1,
                "data": "2024-06-12",
                "horario": 1,
                "sala_reuniao": 1,
            },
            {
                "user": 2,
                "data": "2024-06-13",
                "horario": 1,
                "sala_reuniao": 1,
            },
            {
                "user": 3,
                "data": "2024-06-16",
                "horario": 1,
                "sala_reuniao": 2,
            },
            {
                "user": 4,
                "data": "2024-06-18",
                "horario": 1,
                "sala_reuniao": 2,
            },
            {
                "user": 5,
                "data": "2024-04-12",
                "horario": 8,
                "sala_reuniao": 2,
            },
            {
                "user": 5,
                "data": "2024-06-13",
                "horario": 4,
                "sala_reuniao": 1,
            },
            {
                "user": 5,
                "data": "2024-06-21",
                "horario": 2,
                "sala_reuniao": 1,
            },
            {
                "user": 5,
                "data": "2024-06-13",
                "horario": 5,
                "sala_reuniao": 2,
            },
            {
                "user": 5,
                "data": "2024-06-10",
                "horario": 3,
                "sala_reuniao": 2,
            },
            {
                "user": 5,
                "data": "2024-06-02",
                "horario": 6,
                "sala_reuniao": 2,
            },
            {
                "user": 6,
                "data": "2024-02-13",
                "horario": 3,
                "sala_reuniao": 1,
            },
        ]

        model_data = [
            (ReservaComputador, test_reservas_computadores),
            (ReservaTablet, test_reservas_tablets),
            (ReservaKitTablet, test_reservas_kits_tablets),
            (ReservaOculusVR, test_reservas_oculus_vr),
            (ReservaMesaTrabalho, test_reservas_mesa_trabalho),
            (ReservaSalaReuniao, test_reservas_sala_reuniao),
        ]

        for model, data in model_data:
            for item in data:
                item["user"] = User.objects.get(pk=item["user"])
                if model == ReservaComputador:
                    item["computador"] = Computador.objects.get(numero=item.pop("computador"))
                elif model == ReservaTablet:
                    item["tablet"] = Tablet.objects.get(numero=item.pop("tablet"))
                elif model == ReservaKitTablet:
                    item["kit_tablet"] = KitTablet.objects.get(numero=item.pop("kit_tablet"))
                elif model == ReservaOculusVR:
                    item["oculus_vr"] = OculusVR.objects.get(numero=item.pop("oculus_vr"))
                elif model == ReservaMesaTrabalho:
                    item["mesa_trabalho"] = MesaTrabalho.objects.get(numero=item.pop("mesa_trabalho"))
                elif model == ReservaSalaReuniao:
                    item["sala_reuniao"] = SalaReuniao.objects.get(numero=item.pop("sala_reuniao"))

                model.objects.update_or_create(**item)
