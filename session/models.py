from django.db import models
from django.forms.models import model_to_dict

class Session(models.Model):
    meet = models.ForeignKey("meet.Meet", on_delete=models.CASCADE)   
    bodyweight = models.IntegerField()
    letter = models.CharField(max_length=1)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.bodyweight) + self.letter

class Athlete(models.Model):
    session = models.ForeignKey("Session", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    date_of_birth = models.DateField()
    gender = models.BooleanField()
    bodyweight = models.FloatField()
    affiliation = models.CharField(max_length=3)

    def __str__(self):
        return self.name
    
    def get_dict(self):
        return model_to_dict(self)