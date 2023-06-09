from django.db import models

import workouts.models
from workouts.models import Workout

# Create your models here.
class Calendar(models.Model):
    id = models.AutoField(primary_key=True)
    Date = models.DateField()
    workout = models.ForeignKey(workouts.models.Workout, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)