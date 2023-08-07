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

class StaffForm(forms.Form):
    apellido = forms.CharField(label="Apellido Staff", max_length=50, required=True)
    email = forms.IntegerField(label="Email", required=True)

class UsuariosForm(form.Form):
    apellido = forms.CharField(label="Apellido Usuario", max_length=50, required=True)
    email = forms.IntegerField(label="Email", required=True)