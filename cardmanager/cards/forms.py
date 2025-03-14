from django import forms
from .models import Card
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['player_name', 'team', 'card_brand', 'card_number', 'front_image', 'back_image', 'for_sale']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
