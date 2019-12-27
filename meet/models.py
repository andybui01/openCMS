from django.contrib.auth import get_user_model
from django.db import models

class Meet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name