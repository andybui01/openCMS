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
    
    def create_lifts(self):
        for i in range(1,7):
            self.lift_set.create(attempt=i)
        return

class Lift(models.Model):
    athlete = models.ForeignKey("Athlete", on_delete=models.CASCADE)
    attempt = models.IntegerField(default=1)
    weight = models.IntegerField(default=0)
    result = models.NullBooleanField(default=None)
    changes = models.IntegerField(default=0)