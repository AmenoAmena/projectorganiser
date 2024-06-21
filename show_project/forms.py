from django import forms
from authentication.models import Project

class SeeForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('token',)

        widgets = {
            'token':forms.TextInput(attrs={'autocomplete':'off'}),
        }



