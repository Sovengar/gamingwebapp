from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Seller

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
            attrs={ 'help_text': None
            }
        ),
        'email': forms.EmailInput(
            attrs={ 
            }
        )
    }

class ProfileUserUpdateForm(forms.ModelForm):
    email = forms.EmailInput()
    class Meta:
        model = User 
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']

class SellerRegisterForm(forms.ModelForm):
    zip = forms.CharField(max_length=5)
    birth_date = forms.DateField(error_messages={'required': 'Please enter your name'}, widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date', 'class': "input", 'placeholder': "Ex.: dd/mm/aaaa", "OnKeyPress":"mask('##/##/####', this)"}))
    terms = forms.BooleanField(required=True)
    class Meta:
        model = Seller 
        fields = ['birth_date', 'country', 'zip', 'street_and_number', 'phone_number', 'city']
        labels = {}
        widgets = {
            'street_and_number':forms.TextInput(attrs={'placeholder': 'Street and number'}),
            'phone_number':forms.TextInput(attrs={'placeholder': 'Ex +34 123 44 55 66'})
        }

class SellerUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['first_name', 'last_name']