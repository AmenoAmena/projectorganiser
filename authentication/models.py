from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feature(models.Model):
    feature_add = models.CharField(max_length=80)
    feature_done = models.BooleanField(default=False)

    def __str__(self):
        return self.feature_add


class Project(models.Model):
    name = models.CharField(max_length=80,unique=True)
    link = models.URLField()
    notes = models.TextField(blank=True)
    features = models.ManyToManyField(Feature, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

