from django import forms
from authentication.models import Project,Feature

class project_form(forms.ModelForm):
    class Meta:
        model = Project
        fields = {'link','notes','features'}

        widgets = {
            'link':forms.TextInput(attrs={'autocomplete':'off'}),
            'notes':forms.Textarea(attrs={'autocomplete':'off'}),
        }
        

class add_project_form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("name","link",'token')
        
        labels = {
            'name':'Project Name',
            'link':'Github Link'
        }

        widgets = {
            'name':forms.TextInput(attrs={'autocomplete':'off'}),
            'link':forms.TextInput(attrs={'autocomplete':'off'}),
            'token':forms.TextInput(attrs={'autocomplete':'off','placeholder':'XXXX-XXXX-XXXX-XXXX','id':'token-form'})
        }

class feature_add(forms.ModelForm):
    class Meta:
        model = Feature
        fields = {'feature_add'}

        widgets = {
            'feature_add':forms.TextInput(attrs={'autocomplete':'off'})
        }

class note_add(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['notes']
        widgets = {
            'notes': forms.Textarea(attrs={'autocomplete':'off'}),  
        }
