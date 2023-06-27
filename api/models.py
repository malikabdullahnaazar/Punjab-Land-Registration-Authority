from django.db import models

# Create your models here.
class TestUser(models.Model):
    firstName = models.CharField(max_length=200) 

class phoneModel(models.Model):
    Mobile = models.IntegerField(blank=False)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)
def __str__(self):
        return str(self.Mobile)