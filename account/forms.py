from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Adresse e-mail', max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Adresse e-mail'}))
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))