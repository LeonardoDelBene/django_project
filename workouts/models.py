from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Workout(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    exercises=models.ManyToManyField(to='Exercise', related_name='esercizio')


class Exercise(models.Model):
    id=models.AutoField(primary_key=True)
    workout=models.ForeignKey('Workout', on_delete=models.CASCADE)
    nExercise=models.IntegerField()
    name = models.CharField(max_length=100)
    description=models.TextField(blank=True, null=True)
    sets=models.ManyToManyField(to='Set', related_name='serie')

    def get_nExercise(self):
        return self.nExercise

class Set(models.Model):
    id=models.AutoField(primary_key=True)
    exercise=models.ForeignKey('Exercise', on_delete=models.CASCADE)
    reps=models.IntegerField(blank=True, null=True)
    weight=models.CharField(max_length=30, blank=True, null=True)
    recovery_time=models.IntegerField(blank=True, null=True)
