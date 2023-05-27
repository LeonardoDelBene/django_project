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
        workout = Workout.objects.create(user=user, name=name)
        return redirect('workout_detail', workout_id=workout.id)

    return render(request, 'create_workout.html')


def create_exercise(request, workout_id, nExercise):
    workout = get_object_or_404(Workout, id=workout_id)
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST.get('description')
        Exercise.objects.filter(workout=workout, nExercise=nExercise).update(name=name, description=description)
        exercise = Exercise.objects.filter(workout=workout, nExercise=nExercise).first()
        return redirect('exercise_detail', workout_id=workout_id, exercise_id=exercise.id)
    exercise = Exercise.objects.create(workout=workout, nExercise=nExercise)
    context = {
        'workout_id': workout_id,
        'nExercise': nExercise,
        'exercise_id': exercise.id,
    }
    return render(request, 'create_exercise.html', context=context)

def create_set(request,workout_id, exercise_id):
    if request.method == 'POST':
        exercise = Exercise.objects.get(id=exercise_id)
        reps = request.POST.get('reps')
        weight = request.POST.get('weight')
        recovery_time = request.POST.get('recovery_time')

        set_obj = Set.objects.create(exercise=exercise, reps=reps, weight=weight, recovery_time=recovery_time)

        return redirect('set_detail',workout_id=workout_id,exercise_id=exercise_id, set_id=set_obj.id)

    exercise = Exercise.objects.get(id=exercise_id)
    context = {
        'exercise_id': exercise.id,
        'workout_id': workout_id,
    }
    return render(request, 'create_set.html', context)

def exercise_detail(request, workout_id, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    context = {
        'exercise': exercise,
        'workout_id': workout_id,
    }
    return render(request, 'exercise_detail.html', context)

def workout_detail(request, workout_id):
    n = get_object_or_404(Exercise, pk=workout_id).nExercise + 1
    context={
        'workout_id': workout_id,
        'nes': n
    }
    return render(request, 'workout_detail.html',context=context)

def set_detail(request,workout_id, exercise_id, set_id):
    set_obj = get_object_or_404(Set, pk=set_id)
    context = {
        'set': set_obj,
        'workout_id': workout_id,
        'exercise_id': exercise_id,
    }
    return render(request, 'set_detail.html', context=context)