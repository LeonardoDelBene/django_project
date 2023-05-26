from django.urls import path

from workouts.views import create_workout, create_exercise, create_set, exercise_detail, workout_detail, set_detail

urlpatterns = [
    path('create_workout/', create_workout, name='create_workout'),
    path('create_exercise/<int:workout_id>/', create_exercise, name='create_exercise'),
    path('create_set/<int:exercise_id>/', create_set, name='create_set'),
    path('exercise_detal/<int:exercise_id>/', exercise_detail, name='exercise_detail'),
    path('workout_detail/<int:workout_id>/', workout_detail, name='workout_detail'),
    path('set_detail/<int:set_id>/', set_detail, name='set_detail')
]