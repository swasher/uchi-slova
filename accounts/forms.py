# coding: utf-8

from django import forms
from accounts.models import CustomizedUser

# DEPRECATED
# class AuthenticationForm(forms.Form):
#     """
#     Login form
#     """
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail Address'}),
#         label="Email")
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
#         label="Password")
#
#     class Meta:
#         fields = ['email', 'password']


class UserCreationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    # Настройки для отображения полей формы
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'E-mail Address'}),
        label="Email")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),
        label="Password")

    # Указываем, какая модель используется для формы, и какой набор полей
    class Meta:
        model = CustomizedUser
        fields = ['email', 'password']

    def clean(self):
        """
        Verifies that the values entered into the password fields match

        NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
        """
        cleaned_data = super(UserCreationForm, self).clean()
        return self.cleaned_data

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
