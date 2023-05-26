from django.db import models

# Create your models here.
class Goal(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    goal=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()
    completed=models.BooleanField(default=False)