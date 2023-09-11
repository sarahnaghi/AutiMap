
# Create your models here.

from django.contrib.auth.models import User 
from django.db import models

class SpecialistProfile(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE ,primary_key=True)

 is_accepted_by_admin = models.BooleanField(default=False)
 is_specialist = models.BooleanField(default=False)
 
 gender_choices = (('Male','Male'),('Female','Female'))

 specialist_image = models.ImageField(upload_to='images/')
 major = models.CharField(max_length=1000)
 city = models.CharField(max_length=2048)
 gender = models.CharField(max_length=128,choices=gender_choices)
 phone_number = models.IntegerField()

 accepet=models.BooleanField(default=False)
 description=  models.TextField(blank=True)
 experience=  models.TextField(blank=True)
 education=  models.TextField(blank=True)
 linked_in=  models.URLField(blank=True)


 





