from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.full_name

# Create your models here.
