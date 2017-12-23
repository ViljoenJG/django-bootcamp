from django import forms
from django.core import validators

class MyForm(forms.Form):
    name = forms.CharField(required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))

    email = forms.EmailField(required=True,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))

    text = forms.CharField(required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'}))

    botcatcher = forms.CharField(required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)])
