from django import forms

from .models import ReservaComputador


class ReservaComputadorForm(forms.ModelForm):
    class Meta:
        model = ReservaComputador
        fields = ["computador", "data", "horario"]
        widgets = {
            "computador": forms.Select(attrs={"class": "form-control"}),
            "data": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "horario": forms.Select(attrs={"class": "form-control"}),
        }
