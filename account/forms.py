from django import forms
from.models import User
from django.contrib.auth.password_validation import validate_password

class LoginForm(forms.Form):
    email = forms.EmailField(label='Adresse e-mail', max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Adresse e-mail'}))
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={"placeholder": "Mot de passe"}),
    )
    confirm_password = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirmer le mot de passe"}),
    )

    class Meta:
        model = User
        fields = ("email", "username")
        labels = {
            "email": "Adresse e-mail",
            "username": "Nom d'utilisateur",
        }
        widgets = {
            "email": forms.EmailInput(attrs={"placeholder": "Adresse e-mail"}),
            "username": forms.TextInput(attrs={"placeholder": "Nom d'utilisateur"}),
        }
        help_texts = {
        "username": "",
        }

    def clean_password(self):
        password = self.cleaned_data["password"]
        validate_password(password)
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error(
                "confirm_password",
                "Le mot de passe et la confirmation ne correspondent pas.",
            )
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user