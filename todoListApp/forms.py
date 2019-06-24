from django import forms
from django.forms import ModelForm
from .models import Todo
from django.core.exceptions import NON_FIELD_ERRORS


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "body", "status"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'wrap-input100 validate-input'}),
            'body': forms.TextInput(attrs={'class': 'input100'}),
        }