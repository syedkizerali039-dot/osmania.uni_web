from django.db import models

class Result(models.Model):
    name = models.IntegerField()
    current_date = models.DateField(auto_now=True)

class Marks(models.Model):
    name = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    htno = models.CharField(max_length=255)
    gender = models.IntegerField()
    subject1= models.IntegerField()
    subject2= models.IntegerField()
    subject3= models.IntegerField()
    subject4= models.IntegerField()
    subject5= models.IntegerField()
    subject6= models.IntegerField()

