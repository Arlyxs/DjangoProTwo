from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)


def __str__(self):
    return self.first_name + ' ' + self.last_name + ' ' + self.email
