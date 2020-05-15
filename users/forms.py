from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailInput()
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
        labels = { }
        widgets = {
        'username': forms.TextInput(
            attrs={ 
            }
        ),
        'password1': forms.PasswordInput(
            attrs={  
            }
        ),
        'password2': forms.PasswordInput(
            attrs={ 
            }
        ),
        'email': forms.EmailInput(
            attrs={ 
            }
        )
    }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailInput()
    class Meta:
        model = User 
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']