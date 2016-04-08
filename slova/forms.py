# coding: utf-8

from django import forms
from slova.models import Slova

class AddNewWordForm(forms.ModelForm):

    rus = forms.CharField(
        label="По-русски",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'in russian'})
    )
    eng = forms.CharField(
        label="По-английски",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'in english'})
    )

    class Meta:
        model = Slova
        fields = ['eng', 'rus']