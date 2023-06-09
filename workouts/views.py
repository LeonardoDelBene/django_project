from http.client import HTTPResponse

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.template import context

from .models import Workout, Exercise, Set, Weight_Tracking, Reps_Tracking
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

        exercise = Exercise.objects.filter(workout=workout, nExercise=nExercise).first()
        if exercise is None:
            exercise = Exercise.objects.create(workout=workout, nExercise=nExercise, name=name, description=description)
            return redirect('exercise_detail', workout_id=workout_id, nExercise=nExercise)
        else:

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
        nSet=Set.objects.filter(exercise=exercise).count()+1
        set=Set.objects.create(exercise=exercise,nSet=nSet, reps=reps, weight=weight, recovery_time=recovery_time)

        return redirect('set_detail',workout_id=workout_id, nExercise=nExercise, set_id=set.id)

    context = {
        'nExercise': nExercise,
        'workout_id': workout_id,
    }
    return render(request, 'create_set.html', context)

def exercise_detail(request, workout_id, nExercise):
    exercise = Exercise.objects.get(workout_id=workout_id, nExercise=nExercise)
    sets=Set.objects.filter(exercise=exercise)
    context = {
        'exercise': exercise,
        'workout_id': workout_id,
        'sets': sets,
    }
    return render(request, 'exercise_detail.html', context)

def workout_detail(request, workout_id):
    n = Exercise.objects.filter(workout_id=workout_id).count() + 1
    workout=Workout.objects.get(id=workout_id)
    exercises=Exercise.objects.filter(workout_id=workout_id)
    context={
        'workout': workout,
        'exercises': exercises,
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





def set_weight(request,workout_id, nExercise, set_id):
    if(request.method=='POST'):
        set = Set.objects.get(id=set_id)
        set.weight = request.POST.get('weight')
        weight_track= Weight_Tracking.objects.create(set=set, weight=set.weight)
        set.save()
        exercise = Exercise.objects.get(workout_id=workout_id, nExercise=nExercise)
        sets = Set.objects.filter(exercise=exercise, )
        context = {
            'sets': sets,
            'workout_id': workout_id,
            'nExercise': nExercise,
        }
        return render(request, 'get_sets.html', context=context)
    context = {
        'workout_id': workout_id,
        'nExercise': nExercise,
        'set_id': set_id,
    }
    return render(request, 'set_weight.html', context=context)

def get_weight_history(request,workout_id, nExercise ,set_id):
    set = Set.objects.get(id=set_id)
    weight_track = Weight_Tracking.objects.filter(set=set)
    context = {
        'weight_track': weight_track,
        'set': set,
        'workout_id': workout_id,
        'nExercise': nExercise,
    }
    return render(request, 'get_weight_history.html', context=context)

def set_reps(request,workout_id, nExercise, set_id):
    if(request.method=='POST'):
        set = Set.objects.get(id=set_id)
        set.reps = request.POST.get('reps')
        set.save()
        Reps_Tracking.objects.create(set=set, reps=set.reps)
        exercise = Exercise.objects.get(workout_id=workout_id, nExercise=nExercise)
        sets = Set.objects.filter(exercise=exercise, )
        context = {
            'sets': sets,
            'workout_id': workout_id,
            'nExercise': nExercise,
        }
        return render(request, 'get_sets.html', context=context)
    context = {
        'workout_id': workout_id,
        'nExercise': nExercise,
        'set_id': set_id,
    }
    return render(request, 'set_reps.html', context=context)

def get_reps_history(request,workout_id, nExercise ,set_id):
    set = Set.objects.get(id=set_id)
    reps_track = Reps_Tracking.objects.filter(set=set)
    context = {
        'reps_track': reps_track,
        'set': set,
        'workout_id': workout_id,
        'nExercise': nExercise,
    }
    return render(request, 'get_reps_history.html', context=context)

def delete_reps_history(request,workout_id, nExercise ,set_id, reps_id):
    Reps_Tracking.delete(self=Reps_Tracking.objects.get(id=reps_id))
    set = Set.objects.get(id=set_id)
    reps_track = Reps_Tracking.objects.filter(set=set)
    context = {
        'reps_track': reps_track,
        'set': set,
        'workout_id': workout_id,
        'nExercise': nExercise,
    }
    return render(request, 'get_reps_history.html', context=context)

def delete_weight_history(request,workout_id, nExercise ,set_id, weight_id):
    Weight_Tracking.delete(self=Weight_Tracking.objects.get(id=weight_id))
    set = Set.objects.get(id=set_id)
    weight_track = Weight_Tracking.objects.filter(set=set)
    context = {
        'weight_track': weight_track,
        'set': set,
        'workout_id': workout_id,
        'nExercise': nExercise,
    }
    return render(request, 'get_weight_history.html', context=context)

def delete_workout(request, workout_id):
    Workout.delete(self=Workout.objects.get(id=workout_id))
    workouts = Workout.objects.filter(user=request.user)
    context = {
        'workouts': workouts,
    }
    return render(request, 'get_workouts.html', context=context)

def delete_exercise(request, workout_id, nExercise):
    Exercise.delete(self=Exercise.objects.get(workout_id=workout_id, nExercise=nExercise))
    n = Exercise.objects.filter(workout_id=workout_id).count() + 1
    workout = Workout.objects.get(id=workout_id)
    exercises = Exercise.objects.filter(workout_id=workout_id)
    context = {
        'workout': workout,
        'exercises': exercises,
        'workout_id': workout_id,
        'nes': n
    }
    return render(request, 'workout_detail.html', context=context)
