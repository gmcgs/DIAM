from django import forms
from .models import Aluno
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class OptionForm(forms.Form):
    opcao = forms.CharField(label="Opcao", max_length=100)

class AlunoForm(forms.ModelForm):
    nome = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Aluno
        fields = ['curso', "grupo"]

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['nome'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )
        aluno = super().save(commit=False)
        aluno.user = user
        if commit:
            aluno.save()
        return aluno


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username')
    password = forms.CharField(label='Password')
