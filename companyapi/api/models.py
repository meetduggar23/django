from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()

    TYPE_CHOICES = [
        ('IT', 'IT'),
        ('Finance', 'Finance'),
        ('Healthcare', 'Healthcare'),
    ]

    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    added_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

class Employee(models.Model):

    POSITION_CHOICES = [
        ('Manager', 'Manager'),
        ('Developer', 'Developer'),
        ('Tester', 'Tester'),
        ('HR', 'HR'),
        ('Intern', 'Intern'),
    ]

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)

    def __str__(self):
        return self.name


