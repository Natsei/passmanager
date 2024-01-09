from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Site

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['nom', 'url', 'identifiant']
        # Note: 'mot_de_passe' n'est pas inclus ici car il est géré séparément

    mot_de_passe = forms.CharField(widget=forms.PasswordInput(), required=False)

    def save(self, commit=True):
        site = super().save(commit=False)
        if self.cleaned_data['mot_de_passe']:
            site.set_mot_de_passe(self.cleaned_data['mot_de_passe'])
        if commit:
            site.save()
        return site

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requis. Entrez une adresse email valide.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
