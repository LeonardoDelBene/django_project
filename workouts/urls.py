from django.urls import path

from workouts.views import create_workout, create_exercise, create_set, exercise_detail, workout_detail, set_detail, \
    get_workouts, get_exercises

urlpatterns = [
    path('create_workout/', create_workout, name='create_workout'),
    path('create_exercise/<int:workout_id>/<int:nExercise>/', create_exercise, name='create_exercise'),
    path('create_set/<int:workout_id>/<int:nExercise>/', create_set, name='create_set'),
    path('exercise_detail/<int:workout_id>/<int:nExercise>/', exercise_detail, name='exercise_detail'),
    path('workout_detail/<int:workout_id>/', workout_detail, name='workout_detail'),
    path('set_detail/<int:workout_id>/<int:nExercise>/<int:set_id>/', set_detail, name='set_detail'),
    path('get_workouts', get_workouts, name='get_workouts'),
    path('get_exercises/<int:workout_id>/',get_exercises,name='exercise_list'),
]