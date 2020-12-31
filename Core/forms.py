from django import forms
from .models import Text
from django.forms import ModelForm

class TextForm(ModelForm):
    
    class Meta:
        model = Text
        fields = ("inputfiled",)

        widgets = {
            "inputfiled" : forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Title",
            }),
        }