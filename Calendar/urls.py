from django.contrib import admin
from django.urls import path, include

from Calendar.views import calendar_view, add_workout

urlpatterns = [
    path('calendar/',calendar_view, name='calendar'),
    path('add_workout/',add_workout, name='add_workout'),
]