from http.client import HTTPResponse

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.template import context

from .models import Workout, Exercise, Set
from django.shortcuts import render, get_object_or_404


def create_workout(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST['name']
        workout = Workout.objects.filter(user=user, name=name).first()
        if workout is None:
            workout = Workout.objects.create(user=user, name=name)
            return redirect('workout_detail', workout_id=workout.id)
        else:
            return redirect('workout_detail', workout_id=workout.id)


    return render(request, 'create_workout.html')


def create_exercise(request, workout_id, nExercise):
    workout = Workout.objects.get(id=workout_id)
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST.get('description')

        # Verifica se l'esercizio esiste già
        exercise = Exercise.objects.filter(workout=workout, nExercise=nExercise).first()
        if exercise is None:
            exercise = Exercise.objects.create(workout=workout, nExercise=nExercise, name=name, description=description)
            return redirect('exercise_detail', workout_id=workout_id, nExercise=nExercise)
        else:
            # L'esercizio esiste già, puoi gestire questa situazione a tua discrezione
            # Ad esempio, puoi mostrare un messaggio di errore o reindirizzare a un'altra pagina
            return redirect('exercise_detail', workout_id=workout_id, nExercise=nExercise)

    context = {
        'workout_id': workout_id,
        'nExercise': nExercise,
    }
    return render(request, 'create_exercise.html', context=context)


def create_set(request,workout_id, nExercise):
    if request.method == 'POST':
        exercise = Exercise.objects.get(workout_id=workout_id, nExercise=nExercise)
        reps = request.POST.get('reps')
        weight = request.POST.get('weight')
        recovery_time = request.POST.get('recovery_time')

        set=Set.objects.create(exercise=exercise, reps=reps, weight=weight, recovery_time=recovery_time)

        return redirect('set_detail',workout_id=workout_id, nExercise=nExercise, set_id=set.id)

    context = {
        'nExercise': nExercise,
        'workout_id': workout_id,
    }
    return render(request, 'create_set.html', context)

def exercise_detail(request, workout_id, nExercise):
    exercise = Exercise.objects.get(workout_id=workout_id, nExercise=nExercise)
    context = {
        'exercise': exercise,
        'workout_id': workout_id,
    }
    return render(request, 'exercise_detail.html', context)

def workout_detail(request, workout_id):
    n = Exercise.objects.filter(workout_id=workout_id).count() + 1
    context={
        'workout_id': workout_id,
        'nes': n
    }
    return render(request, 'workout_detail.html',context=context)

def set_detail(request,workout_id, nExercise, set_id):
    set_obj = get_object_or_404(Set, pk=set_id)
    context = {
        'set': set_obj,
        'workout_id': workout_id,
        'nExercise': nExercise,
    }
    return render(request, 'set_detail.html', context=context)

def get_workouts(request):
    workouts = Workout.objects.filter(user=request.user)
    context = {
        'workouts': workouts,
    }
    return render(request, 'get_workouts.html', context=context)

def get_exercises(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    exercises = Exercise.objects.filter(workout=workout)
    context = {
        'exercises': exercises,
        'workout': workout,
    }
    return render(request, 'get_exercises.html', context=context)

def get_sets(request, workout_id, nExercise):
    exercise = Exercise.objects.get(workout_id=workout_id, nExercise=nExercise)
    sets = Set.objects.filter(exercise=exercise,)
    context = {
        'sets': sets,
        'workout_id': workout_id,
        'nExercise': nExercise,
    }
    return render(request, 'get_sets.html', context=context)