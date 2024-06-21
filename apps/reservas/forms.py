from django import forms

from .models import (
    ReservaComputador,
    ReservaKitTablet,
    ReservaMesaTrabalho,
    ReservaOculusVR,
    ReservaSalaReuniao,
    ReservaTablet,
)


class ReservaComputadorForm(forms.ModelForm):
    class Meta:
        model = ReservaComputador
        fields = ["computador", "data", "horario"]
        widgets = {
            "computador": forms.Select(attrs={"class": "form-control"}),
            "data": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "horario": forms.Select(attrs={"class": "form-control"}),
        }


class ReservaTabletForm(forms.ModelForm):
    class Meta:
        model = ReservaTablet
        fields = ["tablet", "data", "horario"]
        widgets = {
            "tablet": forms.Select(attrs={"class": "form-control"}),
            "data": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "horario": forms.Select(attrs={"class": "form-control"}),
        }


class ReservaKitTabletForm(forms.ModelForm):
    class Meta:
        model = ReservaKitTablet
        fields = ["kit_tablet", "data", "horario"]
        widgets = {
            "kit_tablet": forms.Select(attrs={"class": "form-control"}),
            "data": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "horario": forms.Select(attrs={"class": "form-control"}),
        }


class ReservaOculusVRForm(forms.ModelForm):
    class Meta:
        model = ReservaOculusVR
        fields = ["oculus_vr", "data", "horario"]
        widgets = {
            "oculus_vr": forms.Select(attrs={"class": "form-control"}),
            "data": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "horario": forms.Select(attrs={"class": "form-control"}),
        }


class ReservaMesaTrabalhoForm(forms.ModelForm):
    class Meta:
        model = ReservaMesaTrabalho
        fields = ["mesa_trabalho", "data", "horario"]
        widgets = {
            "mesa_trabalho": forms.Select(attrs={"class": "form-control"}),
            "data": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "horario": forms.Select(attrs={"class": "form-control"}),
        }


class ReservaSalaReuniaoForm(forms.ModelForm):
    class Meta:
        model = ReservaSalaReuniao
        fields = ["sala_reuniao", "data", "horario"]
        widgets = {
            "sala_reuniao": forms.Select(attrs={"class": "form-control"}),
            "data": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "horario": forms.Select(attrs={"class": "form-control"}),
        }
