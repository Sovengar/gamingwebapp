from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.core.validators import RegexValidator
from django.forms import widgets
from .models import Post, Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment 
        fields = ['content']