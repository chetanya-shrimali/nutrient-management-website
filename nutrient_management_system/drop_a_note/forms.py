from django import forms
from django.contrib.auth.models import User
from .models import Note


class ContactForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['name', 'email', 'note', ]
