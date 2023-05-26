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
        exercises = request.POST.getlist('exercises')

        workout = Workout.objects.create(user=user, name=name)
        return redirect('workout_detail', workout_id=workout.id)

    return render(request, 'create_workout.html')

def create_exercise(request, workout_id):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST.get('description')
        workout = get_object_or_404(Workout, id=workout_id)
        exercise = Exercise.objects.create(name=name, description=description, workout=workout)
        context={
            'exercise_id': exercise.id,
        }
        return redirect('exercise_detail', context=context)

    context = {
        'workout_id': workout_id
    }
    return render(request, 'create_exercise.html', context=context)


def create_set(request, exercise_id):
    if request.method == 'POST':
        exercise = Exercise.objects.get(id=exercise_id)
        reps = request.POST.get('reps')
        weight = request.POST.get('weight')
        recovery_time = request.POST.get('recovery_time')

        # Verifica se il campo weight è vuoto
        if weight:
            set_obj = Set.objects.create(exercise=exercise, reps=reps, weight=weight, recovery_time=recovery_time)
        else:
            set_obj = Set.objects.create(exercise=exercise, reps=reps, recovery_time=recovery_time)

        return redirect('set_detail', set_id=set_obj.id)

    exercise = Exercise.objects.get(id=exercise_id)
    context = {
        'exercise': exercise
    }
    return render(request, 'create_set.html', context)



def exercise_detail(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    context = {
        'exercise': exercise
    }
    return render(request, 'exercise_detail.html', context)

def workout_detail(request, workout_id):
    context={
        'workout_id': workout_id
    }
    return render(request, 'workout_detail.html',context=context)

def set_detail(request, set_id):
    set_obj = get_object_or_404(Set, pk=set_id)
    context = {
        'set': set_obj
    }
    return render(request, 'set_detail.html', context=context)