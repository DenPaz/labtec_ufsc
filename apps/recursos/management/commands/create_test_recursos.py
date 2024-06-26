from django.core.management.base import BaseCommand

from ...models import Computador, KitTablet, MesaTrabalho, OculusVR, SalaReuniao, Tablet


class Command(BaseCommand):
    def handle(self, *args, **options):
        test_computadores = [
            {
                "numero": 1,
                "processador": "Intel Core i5",
                "memoria_ram": 8,
                "placa_video": "NVIDIA GeForce GTX 1050",
                "armazenamento": 256,
                "so_principal": "Windows",
                "so_secundario": "Linux",
                "fone_ouvido": True,
            },
            {
                "numero": 2,
                "processador": "Intel Core i7",
                "memoria_ram": 16,
                "placa_video": "NVIDIA GeForce GTX 1060",
                "armazenamento": 512,
                "so_principal": "Linux",
                "fone_ouvido": False,
            },
            {
                "numero": 3,
                "processador": "Intel Core i3",
                "memoria_ram": 4,
                "placa_video": "Intel HD Graphics",
                "armazenamento": 128,
                "so_principal": "Windows",
                "so_secundario": "Linux",
                "fone_ouvido": True,
            },
            {
                "numero": 4,
                "processador": "Intel Core i5",
                "memoria_ram": 8,
                "placa_video": "NVIDIA GeForce GTX 1050",
                "armazenamento": 256,
                "so_principal": "Windows",
                "so_secundario": "Linux",
                "fone_ouvido": True,
            },
            {
                "numero": 5,
                "processador": "Intel Core i7",
                "memoria_ram": 16,
                "placa_video": "NVIDIA GeForce GTX 1060",
                "armazenamento": 512,
                "so_principal": "Linux",
                "fone_ouvido": False,
            },
            {
                "numero": 6,
                "processador": "Intel Core i3",
                "memoria_ram": 4,
                "placa_video": "Intel HD Graphics",
                "armazenamento": 128,
                "so_principal": "Windows",
                "so_secundario": "Linux",
                "fone_ouvido": True,
            },
            {
                "numero": 7,
                "processador": "Intel Core i5",
                "memoria_ram": 8,
                "placa_video": "NVIDIA GeForce GTX 1050",
                "armazenamento": 256,
                "so_principal": "Windows",
                "so_secundario": "Linux",
                "fone_ouvido": True,
            },
            {
                "numero": 8,
                "processador": "Intel Core i7",
                "memoria_ram": 16,
                "placa_video": "NVIDIA GeForce GTX 1060",
                "armazenamento": 512,
                "so_principal": "Linux",
                "fone_ouvido": False,
            },
            {
                "numero": 9,
                "processador": "Intel Core i9",
                "memoria_ram": 32,
                "placa_video": "NVIDIA GeForce RTX 2080",
                "armazenamento": 1024,
                "so_principal": "Windows",
                "so_secundario": "Linux",
                "fone_ouvido": True,
            },
            {
                "numero": 10,
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
                "numero": 1,
                "modelo": "Galaxy Tab S6",
                "marca": "Samsung",
                "tamanho_tela": "10.5",
                "so": "Android",
                "armazenamento": 128,
            },
            {
                "numero": 2,
                "modelo": "Galaxy Tab S6",
                "marca": "Samsung",
                "tamanho_tela": "10.5",
                "so": "Android",
                "armazenamento": 256,
            },
            {
                "numero": 3,
                "modelo": "Galaxy Tab S6",
                "marca": "Samsung",
                "tamanho_tela": "10.5",
                "so": "Android",
                "armazenamento": 512,
            },
            {
                "numero": 4,
                "modelo": "iPad",
                "marca": "Apple",
                "tamanho_tela": "10.2",
                "so": "iOS",
                "armazenamento": 256,
            },
            {
                "numero": 5,
                "modelo": "iPad",
                "marca": "Apple",
                "tamanho_tela": "10.2",
                "so": "iOS",
                "armazenamento": 512,
            },
        ]
        test_kits_tables = [
            {
                "numero": 1,
                "tablet_numero": 4,
                "caneta": True,
                "teclado": True,
                "mouse": False,
            },
            {
                "numero": 2,
                "tablet_numero": 5,
                "caneta": True,
                "teclado": False,
                "mouse": False,
            },
        ]
        test_oculus_vrs = [
            {
                "numero": 1,
                "modelo": "Oculus Rift S",
                "marca": "Oculus",
                "resolucao": "2560x1440",
            },
            {
                "numero": 2,
                "modelo": "Oculus Quest 2",
                "marca": "Oculus",
                "resolucao": "3664x1920",
            },
            {
                "numero": 3,
                "modelo": "Oculus Rift X",
                "marca": "Oculus",
                "resolucao": "2560x1440",
            },
        ]
        test_mesas_trabalho = [
            {
                "numero": 1,
                "monitor": True,
                "mouse_pad": True,
                "fone_ouvido": True,
            },
            {
                "numero": 2,
                "monitor": True,
                "mouse_pad": False,
                "fone_ouvido": False,
            },
            {
                "numero": 3,
                "monitor": False,
                "mouse_pad": False,
                "fone_ouvido": True,
            },
            {
                "numero": 4,
                "monitor": True,
                "mouse_pad": True,
                "fone_ouvido": True,
            },
            {
                "numero": 5,
                "monitor": True,
                "mouse_pad": False,
                "fone_ouvido": False,
            },
            {
                "numero": 6,
                "monitor": False,
                "mouse_pad": False,
                "fone_ouvido": True,
            },
            {
                "numero": 7,
                "monitor": True,
                "mouse_pad": True,
                "fone_ouvido": True,
            },
            {
                "numero": 8,
                "monitor": True,
                "mouse_pad": True,
                "fone_ouvido": True,
            },
            {
                "numero": 9,
                "monitor": True,
                "mouse_pad": True,
                "fone_ouvido": True,
            },
        ]
        test_salas_reuniao = [
            {
                "numero": 1,
                "mesas": 1,
                "cadeiras": 6,
                "projetor": False,
                "quadro": False,
            },
            {
                "numero": 2,
                "mesas": 2,
                "cadeiras": 8,
                "projetor": True,
                "quadro": True,
            },
        ]

        model_data = [
            (Computador, test_computadores),
            (Tablet, test_tablets),
            (KitTablet, test_kits_tables),
            (OculusVR, test_oculus_vrs),
            (MesaTrabalho, test_mesas_trabalho),
            (SalaReuniao, test_salas_reuniao),
        ]

        for model, data in model_data:
            for item in data:
                if model == KitTablet:
                    item["tablet"] = Tablet.objects.get(numero=item.pop("tablet_numero"))
                model.objects.update_or_create(**item)
