from django.db import models
# Create your models here.
from django.db import models
class moview(models.Model):
    name=models.CharField(max_length=20)
    actor=models.CharField(max_length=40)
    def __str__(self):
        return  self.name+" "+self.actor