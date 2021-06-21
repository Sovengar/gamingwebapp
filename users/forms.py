from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.core.validators import RegexValidator
from django.forms import widgets
from .models import Profile, Seller
from appsite.models import Key

class UserRegisterForm(UserCreationForm):
    email = forms.EmailInput()
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
           'username': 'Username',
           'email': 'Email',
        }

class ProfileUserUpdateForm(forms.ModelForm):
    email = forms.EmailInput()
    class Meta:
        model = User 
        fields = ['username', 'email']
        labels = {
            'username': 'Username',
            'email': 'Email'
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']
        labels = {
            
        }

class SellerRegisterForm(forms.ModelForm):
    zip = forms.CharField(max_length=5)
    birth_date = forms.DateField(
        error_messages={'required': 'Please enter your date of birth'}, 
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date', 'class': "input", 'placeholder': "Ex.: dd/mm/aaaa", "OnKeyPress":"mask('##/##/####', this)"})
    )
    terms = forms.BooleanField(required=True)
    authenticator_img = forms.ImageField(help_text='A valid ID Card, Passport or driving license with a photo from both sides')
    class Meta:
        model = Seller 
        fields = ['birth_date', 'country', 'zip', 'street_and_number', 'city', 'phone_number', 'authenticator_img'] #
        labels = {
            'birth_date':'Date of birth',
            'country':'Country',
            'zip':'Zip',
            'street_and_number':'Adress',
            'city':'City',
            'phone_number':'Phone number',
            'authenticator_img':'Choose a photo'
        }
        widgets = {
            'street_and_number':forms.TextInput(attrs={'placeholder': 'Street and number'}),
            'phone_number':forms.TextInput(attrs={'placeholder': 'Ex +34 123 44 55 66'})
        } #

class SellerUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['first_name', 'last_name']
        labels = {
            'first_name':'First name',
            'last_name':'Last name'
        }

class SellKeyForm(forms.ModelForm):
    KEY_VALIDATOR = RegexValidator(regex=r'[A-Z0-9]+-[A-Z0-9]+-[A-Z0-9]+')

    key_value = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'AAAAA-BBBBB-CCCCC'}), validators=[KEY_VALIDATOR])
    class Meta:
        model = Key
        fields = ['key_value', 'game', 'price', 'region']
        
        error_messages = {
            NON_FIELD_ERRORS: {'invalid': 'Invalid form'},
            'key_value': {'invalid': 'This is not a valid value'}
        }

        labels = {
            'key_value':'Key value',
            'price':'Price',
            'game':'Game',
            'region':'Region'
        }

        widgets = {

        }

        help_texts = {
            'price':'We will get a fee of 20% from this price to continue developing a good service to our customers',
        }