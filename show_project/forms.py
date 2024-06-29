from django import forms
from authentication.models import Project
from django.core.exceptions import ValidationError

class TokenField(forms.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 19
        super().__init__(*args, **kwargs)
        self.validators.append(self.validate_format)
        self.widget.attrs.update({'class': 'token-field'})

    def validate_format(self, value):
        if len(value) != 19:
            raise ValidationError(f"{value} is not a valid token")
        parts = value.split('-')
        if len(parts) != 4:
            raise ValidationError(f"{value} is not a valid token")

        for part in parts:
            if len(part) != 4 or not part.isalpha() or not part.isupper():
                raise ValidationError(f"{value} is not a valid token")

    def clean(self, value):
        value = super().clean(value)
        self.validate_format(value)
        return value

class SeeForm(forms.Form):
    token = TokenField()


    