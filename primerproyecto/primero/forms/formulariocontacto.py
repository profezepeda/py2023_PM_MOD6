from django import forms

class FormularioContactoForm(forms.Form):
  nombre = forms.CharField(label="Nombre", max_length=20,
    required=True, 
    widget=forms.TextInput(
      attrs={'placeholder': 'Ingresa tu nombre',
             'class': "form-control"}))
  apellido = forms.CharField(label="Apellido", max_length=20,
    required=True,
    widget=forms.TextInput(
      attrs={'placeholder': 'Ingresa tu apellido',
             'class': "form-control"}))
  edad = forms.IntegerField(label="Edad", required=True,
    min_value=0, max_value=150,
    widget=forms.NumberInput(
      attrs={'placeholder': 'Ingresa tu edad',
            'class': "form-control"}))
  email = forms.EmailField(label="Email", required=True,
    max_length=100,
    widget=forms.EmailInput(
      attrs={'placeholder': 'Ingresa tu email',
             'class': "form-control"}))
  mensaje = forms.CharField(label="Mensaje", required=True,
    widget=forms.Textarea(
      attrs={'placeholder': 'Ingresa tu mensaje',
             'class': "form-control"}))