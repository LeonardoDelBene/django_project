from django.shortcuts import render, redirect
from datetime import datetime, timedelta
import calendar

from Calendar.forms import WorkoutForm
from Calendar.models import Calendar


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
    workouts = Calendar.objects.filter(Date__year=year, Date__month=month)

    # Crea un dizionario per mappare i workout alle date
    workout_dict = {workout.date.day: workout.workout for workout in workouts}

    # Verifica se la richiesta è una richiesta POST per l'aggiunta di un workout
    if request.method == 'POST':
        form = WorkoutForm(request.user, request.POST)
        if form.is_valid():
            workout_name = form.cleaned_data['workout']
            day = form.cleaned_data['day']

            # Recupera o crea l'oggetto Calendar per il giorno specificato
            calendar_obj, created = Calendar.objects.get_or_create(Date__year=year, Date__month=month, Date__day=day)
            calendar_obj.workout = workout_name
            calendar_obj.user = request.user
            calendar_obj.save()

            return redirect('calendar_view')
    else:
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
        'form': form,
    }

    return render(request, 'calendar.html', context)


def generate_month_calendar(year, month):
    # Generare il calendario per il mese specificato
    month_calendar = calendar.monthcalendar(year, month)

    return month_calendar


