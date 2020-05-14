from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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