from django.core.exceptions import ValidationError
import re

class PasswordValidator(object):
    def validate(self, password, user=None):
        val = password
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
        if not re.compile('[@_!#$%^&*()<>?/|}{~:]').search(val):
            raise ValidationError("Does not contains special character: [@_!#$%^&*()<>?/|}{~:]")

    def get_help_text(self):
        return (
            "Your password must contain at least 1 digit, 0-9."
        )

# def validate_password(val):
    # 1. the length: betweeen 8 to 12 char
    # 2. should have: atleast 1 lowercase letters, uppercase letters, 
    # number and special character
    # if len(val) < 8 or len(val) > 12:
    #     raise ValidationError("Length should be between 8 to 12 char")
        
    # # if val does not contain an uppercase letter
    # if not re.search(r'[A-Z]', val):
    #     raise ValidationError("Does not contains uppercase letter")
        
    # # if val does not contain an lowercase letter
    # if not re.search(r'[a-z]', val):
    #     raise ValidationError("Does not contains lowercase letter")
        
    # # if val does not contain number
    # if not re.search(r'[0-9]', val):
    #     raise ValidationError("Does not contains number")
        
    # # if val does not contain special character
    # if not re.search(r'[!@#$%^&*(_-+={[;:~`\'<>,.?/"]})]', val):
    #     raise ValidationError("Does not contains special character")