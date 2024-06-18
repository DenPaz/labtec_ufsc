from django.core.management.base import BaseCommand

from ...models import Computador, KitTablet, MesaTrabalho, OculusVR, SalaReuniao, Tablet


class Command(BaseCommand):
    def handle(self, *args, **options):
        test_computadores = [
            {
                "id": 1,
                "processador": "Intel Core i5",
                "memoria_ram": 8,
                "placa_video": "NVIDIA GeForce GTX 1050",
                "armazenamento": 256,
                "so_principal": "Windows",
                "so_secundario": "Linux",
                "fone_ouvido": True,
            },
            {
                "id": 2,
                "processador": "Intel Core i7",
                "memoria_ram": 16,
                "placa_video": "NVIDIA GeForce GTX 1060",
                "armazenamento": 512,
                "so_principal": "Linux",
                "fone_ouvido": False,
            },
            {
                "id": 3,
                "processador": "Intel Core i3",
                "memoria_ram": 4,
                "placa_video": "Intel HD Graphics",
                "armazenamento": 128,
                "so_principal": "Windows",
                "so_secundario": "Linux",
                "fone_ouvido": True,
            },
            {
                "id": 4,
                "processador": "Intel Core i5",
                "memoria_ram": 8,
                "placa_video": "NVIDIA GeForce GTX 1050",
                "armazenamento": 256,
                "so_principal": "Windows",
                "so_secundario": "Linux",
                "fone_ouvido": True,
            },
            {
                "id": 5,
                "processador": "Intel Core i7",
                "memoria_ram": 16,
                "placa_video": "NVIDIA GeForce GTX 1060",
                "armazenamento": 512,
                "so_principal": "Linux",
                "fone_ouvido": False,
            },
            {
                "id": 6,
                "processador": "Intel Core i3",
                "memoria_ram": 4,
                "placa_video": "Intel HD Graphics",
                "armazenamento": 128,
                "so_principal": "Windows",
                "so_secundario": "Linux",
                "fone_ouvido": True,
            },
            {
                "id": 7,
                "processador": "Intel Core i5",
                "memoria_ram": 8,
                "placa_video": "NVIDIA GeForce GTX 1050",
                "armazenamento": 256,
                "so_principal": "Windows",
                "so_secundario": "Linux",
                "fone_ouvido": True,
            },
            {
                "id": 8,
                "processador": "Intel Core i7",
                "memoria_ram": 16,
                "placa_video": "NVIDIA GeForce GTX 1060",
                "armazenamento": 512,
                "so_principal": "Linux",
                "fone_ouvido": False,
            },
            {
                "id": 9,
                "processador": "Intel Core i9",
                "memoria_ram": 32,
                "placa_video": "NVIDIA GeForce RTX 2080",
                "armazenamento": 1024,
                "so_principal": "Windows",
                "so_secundario": "Linux",
                "fone_ouvido": True,
            },
            {
                "id": 10,
                "processador": "Intel Core i9",
                "memoria_ram": 64,
                "placa_video": "NVIDIA GeForce RTX 4090",
                "armazenamento": 2048,
                "so_principal": "Windows",
                "fone_ouvido": True,
            },
        ]
        test_tablets = [
            {
                "id": 1,
                "modelo": "Galaxy Tab S6",
                "marca": "Samsung",
                "tamanho_tela": "10.5",
                "so": "Android",
                "armazenamento": 128,
            },
            {
                "id": 2,
                "modelo": "Galaxy Tab S6",
                "marca": "Samsung",
                "tamanho_tela": "10.5",
                "so": "Android",
                "armazenamento": 256,
            },
            {
                "id": 3,
                "modelo": "Galaxy Tab S6",
                "marca": "Samsung",
                "tamanho_tela": "10.5",
                "so": "Android",
                "armazenamento": 512,
            },
            {
                "id": 4,
                "modelo": "iPad",
                "marca": "Apple",
                "tamanho_tela": "10.2",
                "so": "iOS",
                "armazenamento": 256,
            },
            {
                "id": 5,
                "modelo": "iPad",
                "marca": "Apple",
                "tamanho_tela": "10.2",
                "so": "iOS",
                "armazenamento": 512,
            },
        ]

        for test_computador in test_computadores:
            Computador.objects.update_or_create(
                **test_computador,
            )

        for test_tablet in test_tablets:
            Tablet.objects.update_or_create(
                **test_tablet,
            )

        test_kits_tables = [
            {
                "id": 1,
                "tablet": Tablet.objects.get(id=4),
                "caneta": True,
                "teclado": True,
                "mouse": False,
            },
            {
                "id": 2,
                "tablet": Tablet.objects.get(id=5),
                "caneta": True,
                "teclado": False,
                "mouse": False,
            },
        ]

        for test_kit_table in test_kits_tables:
            KitTablet.objects.update_or_create(
                **test_kit_table,
            )

        test_oculus_vrs = [
            {
                "id": 1,
                "modelo": "Oculus Rift S",
                "marca": "Oculus",
                "resolucao": "2560x1440",
            },
            {
                "id": 2,
                "modelo": "Oculus Quest 2",
                "marca": "Oculus",
                "resolucao": "3664x1920",
            },
            {
                "id": 3,
                "modelo": "Oculus Rift X",
                "marca": "Oculus",
                "resolucao": "2560x1440",
            },
        ]
        test_mesas_trabalho = [
            {
                "id": 1,
                "monitor": True,
                "mouse_pad": True,
                "fone_ouvido": True,
            },
            {
                "id": 2,
                "monitor": True,
                "mouse_pad": False,
                "fone_ouvido": False,
            },
            {
                "id": 3,
                "monitor": False,
                "mouse_pad": False,
                "fone_ouvido": True,
            },
            {
                "id": 4,
                "monitor": True,
                "mouse_pad": True,
                "fone_ouvido": True,
            },
            {
                "id": 5,
                "monitor": True,
                "mouse_pad": False,
                "fone_ouvido": False,
            },
            {
                "id": 6,
                "monitor": False,
                "mouse_pad": False,
                "fone_ouvido": True,
            },
            {
                "id": 7,
                "monitor": True,
                "mouse_pad": True,
                "fone_ouvido": True,
            },
            {
                "id": 8,
                "monitor": True,
                "mouse_pad": True,
                "fone_ouvido": True,
            },
            {
                "id": 9,
                "monitor": True,
                "mouse_pad": True,
                "fone_ouvido": True,
            },
        ]
        test_salas_reuniao = [
            {
                "id": 1,
                "mesas": 1,
                "cadeiras": 6,
                "projetor": False,
                "quadro": False,
            },
            {
                "id": 2,
                "mesas": 2,
                "cadeiras": 8,
                "projetor": True,
                "quadro": True,
            },
        ]

        for test_oculus_vr in test_oculus_vrs:
            OculusVR.objects.update_or_create(
                **test_oculus_vr,
            )

        for test_mesa_trabalho in test_mesas_trabalho:
            MesaTrabalho.objects.update_or_create(
                **test_mesa_trabalho,
            )

        for test_sala_reuniao in test_salas_reuniao:
            SalaReuniao.objects.update_or_create(
                **test_sala_reuniao,
            )
