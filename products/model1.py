
from django.db import models

class publisher(models.Model):
    name = models.CharField(max_length=255)

class Books(models.Model):
    name = models.CharField(max_length=255)
    Authors=models.ManyToManyField(Authors,blank=True,on_delete=models.CASCADE,)
    publisher=models.ForeignKey(publisher,blank=True,on_delete=models.CASCADE,null=True)

class Authors(models.Model):
    name = models.CharField(max_length=255)

class Authors_Profile(models.Model):
    name = models.CharField(max_length=255)
    Authors=models.OneToOneField(Authors,)



