from django import forms

from .models import Escola

from django.core.mail import send_mail
from django.conf import settings


from .mail import send_mail_template

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
