from django import forms

from .models import Computador, KitTablet, MesaTrabalho, OculusVR, SalaReuniao, Tablet


class ComputadorForm(forms.ModelForm):
    class Meta:
        model = Computador
        fields = [
            "numero",
            "processador",
            "memoria_ram",
            "placa_video",
            "armazenamento",
            "so_principal",
            "so_secundario",
            "fone_ouvido",
            "danificado",
        ]
        widgets = {
            "numero": forms.NumberInput(attrs={"class": "form-control"}),
            "processador": forms.TextInput(attrs={"class": "form-control"}),
            "memoria_ram": forms.NumberInput(attrs={"class": "form-control"}),
            "placa_video": forms.TextInput(attrs={"class": "form-control"}),
            "armazenamento": forms.NumberInput(attrs={"class": "form-control"}),
            "so_principal": forms.Select(attrs={"class": "form-control"}),
            "so_secundario": forms.Select(attrs={"class": "form-control"}),
            "fone_ouvido": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "danificado": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class TabletForm(forms.ModelForm):
    class Meta:
        model = Tablet
        fields = [
            "numero",
            "modelo",
            "marca",
            "tamanho_tela",
            "so",
            "armazenamento",
            "danificado",
        ]
        widgets = {
            "numero": forms.NumberInput(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "marca": forms.TextInput(attrs={"class": "form-control"}),
            "tamanho_tela": forms.NumberInput(attrs={"class": "form-control"}),
            "so": forms.Select(attrs={"class": "form-control"}),
            "armazenamento": forms.NumberInput(attrs={"class": "form-control"}),
            "danificado": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class KitTabletForm(forms.ModelForm):
    class Meta:
        model = KitTablet
        fields = [
            "numero",
            "tablet",
            "caneta",
            "teclado",
            "mouse",
            "danificado",
        ]
        widgets = {
            "numero": forms.NumberInput(attrs={"class": "form-control"}),
            "tablet": forms.Select(attrs={"class": "form-control"}),
            "caneta": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "teclado": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "mouse": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "danificado": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class OculusVRForm(forms.ModelForm):
    class Meta:
        model = OculusVR
        fields = [
            "numero",
            "marca",
            "resolucao",
            "danificado",
        ]
        widgets = {
            "numero": forms.NumberInput(attrs={"class": "form-control"}),
            "marca": forms.TextInput(attrs={"class": "form-control"}),
            "resolucao": forms.TextInput(attrs={"class": "form-control"}),
            "danificado": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class MesaTrabalhoForm(forms.ModelForm):
    class Meta:
        model = MesaTrabalho
        fields = [
            "numero",
            "monitor",
            "mouse_pad",
            "fone_ouvido",
        ]
        widgets = {
            "numero": forms.NumberInput(attrs={"class": "form-control"}),
            "monitor": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "mouse_pad": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "fone_ouvido": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class SalaReuniaoForm(forms.ModelForm):
    class Meta:
        model = SalaReuniao
        fields = [
            "numero",
            "mesas",
            "cadeiras",
            "projetor",
            "quadro",
        ]
        widgets = {
            "numero": forms.NumberInput(attrs={"class": "form-control"}),
            "mesas": forms.NumberInput(attrs={"class": "form-control"}),
            "cadeiras": forms.NumberInput(attrs={"class": "form-control"}),
            "projetor": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "quadro": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
