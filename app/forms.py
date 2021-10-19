from django import forms
from django.forms import fields
from .models import Image


class UploadForm(forms.ModelForm):
    file = forms.FileField(widget=forms.FileInput(attrs={
        'id': 'file_id'
    }))

    class Meta:
        model = Image
        fields = ("file",)
