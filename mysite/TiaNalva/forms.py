from django import forms

from .models import Escola

class MeuForm(forms.ModelForm):
    class Meta:
        model = Escola
        fields = '__all__'


class ContactTurma(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Mensagem/Dúvida', widget=forms.Textarea
    )