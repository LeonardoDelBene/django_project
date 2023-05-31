from django.urls import path

from workouts.views import create_workout, create_exercise, create_set, exercise_detail, workout_detail, set_detail, \
    get_workouts, get_exercises, get_sets, set_weight, get_weight_history, set_reps, get_reps_history, \
    delete_reps_history, delete_weight_history, delete_workout, delete_exercise

urlpatterns = [
    path('create_workout/', create_workout, name='create_workout'),
    path('create_exercise/<int:workout_id>/<int:nExercise>/', create_exercise, name='create_exercise'),
    path('create_set/<int:workout_id>/<int:nExercise>/', create_set, name='create_set'),
    path('exercise_detail/<int:workout_id>/<int:nExercise>/', exercise_detail, name='exercise_detail'),
    path('workout_detail/<int:workout_id>/', workout_detail, name='workout_detail'),
    path('set_detail/<int:workout_id>/<int:nExercise>/<int:set_id>/', set_detail, name='set_detail'),
    path('get_workouts', get_workouts, name='get_workouts'),
    path('get_exercises/<int:workout_id>/',get_exercises,name='exercise_list'),
    path('get_sets/<int:workout_id>/<int:nExercise>',get_sets,name='set_list'),
    path('set_weight/<int:workout_id>/<int:nExercise>/<int:set_id>/', set_weight, name='set_weight'),
    path('weight_history/<int:workout_id>/<int:nExercise>/<int:set_id>/',get_weight_history,name='weight_history'),
    path('set_reps/<int:workout_id>/<int:nExercise>/<int:set_id>/',set_reps,name='set_reps'),
    path('get_reps_history/<int:workout_id>/<int:nExercise>/<int:set_id>/',get_reps_history,name='reps_history'),
    path('delete_reps_history/<int:workout_id>/<int:nExercise>/<int:set_id>/<int:reps_id>/',delete_reps_history,name='delete_reps_history'),
    path('delete_weight_history/<int:workout_id>/<int:nExercise>/<int:set_id>/<int:weight_id>/',delete_weight_history,name='delete_weight_history'),
    path('delete_workout/<int:workout_id>/',delete_workout,name='delete_workout'),
    path('delete_exercise/<int:workout_id>/<int:nExercise>/',delete_exercise,name='delete_exercise'),
]