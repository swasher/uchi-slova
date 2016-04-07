# coding: utf-8

from django import forms
from django.core.validators import validate_email

from accounts.models import CustomizedUser
from django.contrib.auth.password_validation import validate_password

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


class UserRegistrationForm(forms.ModelForm):
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

    # def clean(self):
    #     """
    #     Verifies that the values entered into the password fields match
    #
    #     NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
    #     """
    #     cleaned_data = super(UserRegistrationForm, self).clean()
    #     return self.cleaned_data

    def clean_email(self):
        data = self.cleaned_data['email']
        validate_email(data)
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        validate_password(data)
        return data

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
