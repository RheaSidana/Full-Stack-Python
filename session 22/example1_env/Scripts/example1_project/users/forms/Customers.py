# from typing import Any
from django import forms
# from django.contrib.auth.models import User
from ..models import CustomUser

class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        widgets ={
            'password': forms.PasswordInput,
        }

    # def clean(self) -> dict[str, Any]:
    #     return super().clean()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password donot match"
            )
        return cleaned_data
