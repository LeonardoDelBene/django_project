from django.shortcuts import render, redirect
from datetime import datetime, timedelta, date
import calendar

from Calendar.forms import WorkoutForm
from Calendar.models import Calendar
from workouts.models import Workout


def calendar_view(request):
    year = int(request.GET.get('year', datetime.now().year))
    month = int(request.GET.get('month', datetime.now().month))

    month_calendar = generate_month_calendar(year, month)

    prev_month = month - 1 if month > 1 else 12
    prev_year = year if month > 1 else year - 1
    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1

    month_name = calendar.month_name[month]

    # Recupera i workout per il mese corrente
    workouts = Calendar.objects.filter(user=request.user, Date__year=year, Date__month=month)

    # Crea un dizionario per mappare i workout alle date
    workout_dict = {}
    for workout in workouts:
        workout_dict[workout.Date.day] = workout.workout.name

    form = WorkoutForm(request.user)



    context = {
        'month_name': month_name,
        'year': year,
        'month_calendar': month_calendar,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'next_year': next_year,
        'next_month': next_month,
        'workout_dict': workout_dict,
        'workouts': workouts,
        'form': form,

    }

    return render(request, 'calendar.html', context)


def generate_month_calendar(year, month):
    # Generare il calendario per il mese specificato
    month_calendar = calendar.monthcalendar(year, month)

    return month_calendar

def add_workout(request):
    if request.method =='POST':
        form = WorkoutForm(request.user, request.POST)
        if form.is_valid():
            user= request.user
            workout = Workout.objects.get(id=form.cleaned_data['workout'].id)
            year = form.cleaned_data['year']
            month = form.cleaned_data['month']
            day = form.cleaned_data['day']
            date = datetime(year, month, day)
            Calendar.objects.create(user=user, workout=workout, Date=date)
            return redirect('calendar')
    else:
        form=WorkoutForm(request.user)
    return render(request, 'add_workout.html', {'form': form})
