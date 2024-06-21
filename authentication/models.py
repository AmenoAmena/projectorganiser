from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import random

class TokenField(models.CharField):
    description = "A formatted text field with the pattern XXXX-XXXX-XXXX-XXXX"

    
    def generate_token(self):
        letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z'
        ]
        result = ""
        for i in range(0,16):
            if i%4 == 0 and i != 0:
                result += "-"
            result += random.choice(letters)
        return result 

    

    def __init__(self, *args, **kwargs):
        self.random_token = self.generate_token()
        kwargs['max_length'] = 19
        kwargs['unique'] = True
        super().__init__(*args, **kwargs)
        self.validators.append(self.validate_format)
    
    
    def validate_format(self, value):
        if len(value) != 19:
            raise ValidationError(f"{value} is not a valid token")
        parts = value.split('-')
        if len(parts) != 4:
            raise ValidationError(f"{value} is not a valid token")
        
        for part in parts:
            if len(part) != 4 or not part.isalpha() or not part.isupper():
                raise ValidationError(f"{value} is not a valid token")  

    
# Create your models here.
class Feature(models.Model):
    feature_add = models.CharField(max_length=80)
    feature_done = models.BooleanField(default=False)

    def __str__(self):
        return self.feature_add


class Project(models.Model):
    name = models.CharField(max_length=80)
    link = models.URLField()
    notes = models.TextField(blank=True)
    features = models.ManyToManyField(Feature, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    token = TokenField()

    def __str__(self):
        return self.name

