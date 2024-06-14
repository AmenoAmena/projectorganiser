from django import forms
from authentication.models import Project

class project_form(forms.ModelForm):
    class Meta:
        model = Project
        fields = {'link','notes','features'}
        
        labels = {
            'link':'Link',
            'notes':'Notes',
            'features':'Features'
        }
        
class add_project_form(forms.ModelForm):
    class Meta:
        model = Project
        fields = {"name"}
        
        labels = {
            'name':'Project Name'
        }