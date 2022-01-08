from django import forms
from django.forms import widgets

from .models import Pic

class PicForm(forms.ModelForm):
    class Meta:
        model = Pic
        fields = ['image', 'caption']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'caption': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'style': 'resize: none; white-space: pre-wrap;'
                }
            )
        }