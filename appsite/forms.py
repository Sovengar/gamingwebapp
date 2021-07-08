from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.core.validators import RegexValidator
from django.forms import widgets
from .models import Opinion

class OpinionForm(forms.ModelForm):
    opinion = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Opinion 
        fields = ['opinion']

