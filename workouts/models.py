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


class Set(models.Model):
    id=models.AutoField(primary_key=True)
    exercise=models.ForeignKey('Exercise', on_delete=models.CASCADE)
    nSet=models.IntegerField(default=0)
    reps=models.IntegerField(blank=True, null=True)
    weight=models.CharField(max_length=30, blank=True, null=True)
    recovery_time=models.IntegerField(blank=True, null=True)
    weight_tracking=models.ManyToManyField(to='Weight_Tracking', related_name='peso')

class Weight_Tracking(models.Model):
    id = models.AutoField(primary_key=True)
    set = models.ForeignKey('Set', on_delete=models.CASCADE, related_name='weight_trackings')
    weight = models.CharField(max_length=30)
    date = models.DateField(auto_now=True)

