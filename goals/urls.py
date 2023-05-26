from django.urls import path
from .views import get_all_goals, create_goals, view_completed_goals

urlpatterns = [
    path('', get_all_goals, name='goals'),
    path('create/', create_goals, name='create_goals'),
    path('viewCompletedGoal/',view_completed_goals, name='view_completed_goals'),
]