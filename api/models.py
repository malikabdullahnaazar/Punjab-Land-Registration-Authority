from django.db import models

# Create your models here.
class TestUser(models.Model):
    firstName = models.CharField(max_length=200) 
    