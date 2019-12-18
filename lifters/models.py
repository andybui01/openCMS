from django.db import models

class Athlete(models.Model):
    name = models.CharField(max_length=60)
    date_of_birth = models.DateField()
    gender = models.BooleanField()
    bodyweight = models.FloatField()
    affiliation = models.CharField(max_length=3)

    def __str__(self):
        return self.name
    
    def get_birth_year(self):
        return self.date_of_birth.year

class Lift(models.Model):
    athlete = models.ForeignKey("Athlete", on_delete=models.CASCADE)
    weight = models.IntegerField()
    attempt = models.IntegerField()
    
    def __str__(self):
        return str(self.weight)
    
