from django import forms
from .models import Comentario

#Formulário de Comentário
class FazerComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }