from django import forms

from .models import Escola

from django.core.mail import send_mail
from django.conf import settings


from .mail import send_mail_template

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MeuForm(forms.ModelForm):
    class Meta:
        model = Escola
        fields = '__all__'


class ContactTurma(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Mensagem', widget=forms.Textarea
    )
    def send_mail(self, turma):
        subject = '[%s] Contato' % turma
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        template_name = 'contact_email.html'
        send_mail_template(
            subject, template_name, context, [settings.CONTACT_EMAIL]
        )


class RegisterForm(UserCreationForm):

    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe usuário com este E-mail')
        return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class EditAccountForm(forms.ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = User.objects.filter(
            email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Já existe usuário com este E-mail')
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']