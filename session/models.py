from django.db import models
from django.forms.models import model_to_dict

class Session(models.Model):
    meet = models.ForeignKey("meet.Meet", on_delete=models.CASCADE)
    bodyweight = models.IntegerField()
    letter = models.CharField(max_length=1)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.bodyweight) + self.letter

    def sorted_athlete_set(self):
        return self.athlete_set.order_by('next_weight')

class Athlete(models.Model):
    session = models.ForeignKey("Session", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    date_of_birth = models.DateField()
    gender = models.BooleanField()
    bodyweight = models.FloatField()
    affiliation = models.CharField(max_length=3)
    next_attempt = models.IntegerField(default=1)
    next_weight = models.IntegerField(default=-1)

    def __str__(self):
        return self.name

    def create_lifts(self):
        for j in range(1,4):
            for i in range(1,7):
                self.lift_set.create(attempt=i,change=j)
        return

    def update_attempt(self, attempt, change, weight):
        lift = self.lift_set.filter(attempt=attempt).filter(change=change).first()
        lift.set_weight(weight)
        lift.save()

        self.next_weight = weight
        self.next_attempt = attempt
        return

    def get_next_lift(self):
        for i in range(1,4):
            if self.lift_set.filter(attempt=self.next_attempt).filter(change=i).first().weight != -1:
                lift = self.lift_set.filter(attempt=self.next_attempt).filter(change=i).first()
            else:
                break
        return lift

    def get_first_change(self):
        return self.lift_set.filter(change=1)

    def get_second_change(self):
        return self.lift_set.filter(change=2)

    def get_third_change(self):
        return self.lift_set.filter(change=3)


class Lift(models.Model):
    athlete = models.ForeignKey("Athlete", on_delete=models.CASCADE)
    attempt = models.IntegerField(default=1)
    weight = models.IntegerField(default=-1)
    result = models.NullBooleanField(default=None)
    change = models.IntegerField(default=1)

    def __str__(self):
        return str(self.weight)

    def set_weight(self, weight):
        self.weight = weight
        return
