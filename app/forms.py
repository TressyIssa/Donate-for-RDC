from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User, Don, Projet

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)

class DonForm(forms.ModelForm):
    """
    
    projet = forms.ModelChoiceField(
        empty_label="choix du projet",
        queryset=Projet.objects.all()
    )
    montant = forms.IntegerField(
        label="Montant (ETH)"
    )
"""

    class Meta:
        model = Don
        fields = ()
    
class ProjetForm(forms.ModelForm):
    
    class Meta:
        model = Projet
        fields = ("name",)

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Adresse email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre email',
            'aria-label': 'Adresse email',
        })
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre mot de passe',
            'aria-label': 'Mot de passe',
        })
    )