from django import forms
from authentication.models import Project,Feature

class project_form(forms.ModelForm):
    class Meta:
        model = Project
        fields = {'link','notes','features'}
        

class add_project_form(forms.ModelForm):
    class Meta:
        model = Project
        fields = {"name","link"}
        
        labels = {
            'name':'Project Name',
            'link':'Github Link'
        }

class feature_add(forms.ModelForm):
    class Meta:
        model = Feature
        fields = {'feature_add'}

