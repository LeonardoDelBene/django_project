from django.contrib import admin

from workouts.models import Workout, Exercise, Set, Weight_Tracking

# Register your models here.
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Set)
admin.site.register(Weight_Tracking)