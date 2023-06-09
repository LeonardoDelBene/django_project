from django.contrib import admin
from django.urls import path, include

from Calendar.views import calendar_view

urlpatterns = [
    path('calendar/',calendar_view, name='calendar'),
    path('add_workout/',calendar_view, name='add_workout'),
]