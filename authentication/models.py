from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=80)
    link = models.URLField()
    notes = models.TextField()
    features = models.CharField(max_length=160)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name