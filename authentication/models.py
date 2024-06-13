from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feature(models.Model):
    feature_add = models.CharField(max_length=80)
    feature_done = models.BooleanField(default=False)

    def __str__(self):
        return self.feature_add

class Project(models.Model):
    name = models.CharField(max_length=80,default="Project")
    link = models.URLField()
    notes = models.TextField()
    features = models.ForeignKey(Feature,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

