from django import forms

class ActivdadForm(forms.Form):
    nombre = forms.CharField(label="Nombre actividad", max_length=50, required=True)
    comision = forms.IntegerField(label="Comision", required=True)
    SERVIDORES = (
        (1, "Arg_"),
        (2, "Br_"),
        (3, "US_"),
    )
    servidor = forms.ChoiceField(label="Servidor elegido", choices=SERVIDORES, required=True)