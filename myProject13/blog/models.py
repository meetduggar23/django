from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100) ##character field
    age = models.IntegerField() ##integer field
    email = models.EmailField() ##email field
    city = models.CharField(max_length=100,default='Unknown') ##character field
    # enrollment_date = models.DateField() ##date field



    # def __str__(self): 
    #     return self.name ##to return the name of the student when
    #                        ##we print the object of the student class.
