
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    location=models.CharField(max_length=255)

class Company_Address(models.Model):
    name = models.CharField(max_length=255)
    Company=models.OneToOneField(Company,blank=True,on_delete=models.CASCADE,)


class Employee(models.Model):
    name = models.CharField(max_length=255)
    potistion=models.CharField(max_length=255)
    Company=models.ForeignKey(Company,blank=True,on_delete=models.CASCADE,)
    Projects=models.ManyToManyField(Projects,blank=True,on_delete=models.CASCADE,)
    
    
class Projects(models.Model):
    title = models.CharField(max_length=255)
    deadline_date=models.DateTimeField()
    


