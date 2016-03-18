# coding: utf-8

from django import forms
from slova.models import Slova

class AddNewWordForm(forms.ModelForm):
    class Meta:
        model = Slova
        fields = ['eng', 'rus']