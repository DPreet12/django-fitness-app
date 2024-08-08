from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    weight = models.CharField(max_length=10, null=True, blank=True)
    height = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Workout(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    date = models.DateField()
    exercise = models.CharField(max_length=255)
    duration = models.DurationField()
    distance = models.CharField(max_length=10, null = True, blank= True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.exercise} on {self.date}"

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_weight = models.CharField(max_length=10, null = True, blank= True)
    target_date = models.DateField()
    target_purpose= models.CharField(max_length=100, null = True, blank= True)




