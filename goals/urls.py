from django.urls import path
from .views import get_all_goals
urlpatterns = [
    path('', get_all_goals, name='goals'),
]