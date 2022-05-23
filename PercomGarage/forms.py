from django.forms import TextInput, EmailInput, NumberInput, FileInput
from django import forms
from PercomGarage.models import Client, Employe, Vehicules


class clientForm(forms.ModelForm):
    vehicule = forms.ModelChoiceField(queryset=Vehicules.objects.all(), widget=forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 900px;',
                'placeholder': 'profile'
            }))

    class Meta:
        model = Client
        fields = "__all__"
        widgets = {
            'nom': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 900px;',
                'placeholder': 'Name'
            }),
            'prenom': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 900px;',
                'placeholder': 'prenom'
            }),
            'adresse': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 900px;',
                'placeholder': 'adresse'
            }),
            'cni': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 900px;',
                'placeholder': 'cni'
            }),
            'telephone': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 900px;',
                'placeholder': 'telephone'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 900px;',
                'placeholder': 'Email'
            }),
            'sex': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 900px;',
                'placeholder': 'sex'
            }),
            'profile': FileInput(attrs={
                'class': "form-control",
                'style': 'max-width: 900px;',
                'placeholder': 'profile'
            }),
        }


class employeeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = "__all__"


class voitureForm(forms.ModelForm):
    class Meta:
        model = Vehicules
        fields = "__all__"
