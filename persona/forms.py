from django import forms
from .models import persona, contacto 
from django.forms import EmailInput


class Formpersona (forms.ModelForm):
    class Meta:
        model = persona
        fields = '__all__'
        
        
        
class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = contacto
        fields = '__all__'
        widgets = {'email': EmailInput(attrs={'type': 'email'}),}