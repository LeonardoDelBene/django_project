# Generated by Django 4.2.1 on 2023-05-26 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_exercise_nexercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='nExercise',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
