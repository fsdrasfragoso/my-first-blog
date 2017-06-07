from django import forms

from .models import Escola

class MeuForm(forms.ModelForm):
    class Meta:
        model = Escola
        fields = '__all__'
