from django import forms
from ..models import DestiantionWeather
from django.core.exceptions import ValidationError
import re

class DestinationWeatherForm(forms.ModelForm):
    
    class Meta:
        model = DestiantionWeather
        fields = ['destination_name', 'admin_secret', 'weather']
        widgets ={
            'admin_secret': forms.PasswordInput,
            'destination_name': forms.TextInput,
        }

    def clean_admin_secret(self):
        admin_secret = self.cleaned_data.get('admin_secret')
        validate_admin_secret(admin_secret)
        return admin_secret


def validate_admin_secret(val):
    # 1. the length: betweeen 8 to 12 char
    # 2. should have: atleast 1 lowercase letters, uppercase letters, 
    # number and special character
    if len(val) < 8 or len(val) > 12:
        raise ValidationError("Length should be between 8 to 12 char")
        
    # if val does not contain an uppercase letter
    if not re.search(r'[A-Z]', val):
        raise ValidationError("Does not contains uppercase letter")
        
    # if val does not contain an lowercase letter
    if not re.search(r'[a-z]', val):
        raise ValidationError("Does not contains lowercase letter")
        
    # if val does not contain number
    if not re.search(r'[0-9]', val):
        raise ValidationError("Does not contains number")
        
    # if val does not contain special character
    if not re.search(r'[!@#$%^&*(_-+={[;:~`\'<>,.?/"]})]', val):
        raise ValidationError("Does not contains special character")


# class DestinationWeatherForm(forms.Form):
#     destination_name = forms.CharField(
#         label="Destination Name",
#         max_length=200
#     )
#     weather = forms.IntegerField(
#         label="Weather (in Celsius)"
#     )
#     admin_secret = forms.CharField(
#         widget=forms.PasswordInput,
#     )
#     # *******