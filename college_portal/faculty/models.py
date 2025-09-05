from django.db import models

class Faculty(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.full_name
