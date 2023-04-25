from django import forms

class FormularioLogin(forms.Form):
  usuario = forms.CharField(label="Usuario", max_length=15,
    required=True, widget=forms.TextInput(
      attrs={'class':'form-control', 'placeholder':'Ingresa tu usuario'}
    ))
  password = forms.CharField(label="Contraseña", max_length=15,
    required=True, widget=forms.PasswordInput(
      attrs={'class':'form-control', 'placeholder':'Ingresa tu contraseña'}
    ))