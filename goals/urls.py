from django.urls import path
from .views import get_all_goals, create_goals, view_completed_goals, view_incompleted_goals, set_goal_completed

urlpatterns = [
    path('', get_all_goals, name='goals'),
    path('create/', create_goals, name='create_goals'),
    path('viewCompletedGoal/',view_completed_goals, name='view_completed_goals'),
    path('viewIncompletedGoal/',view_incompleted_goals, name='view_incomplete_goals'),
    path('setGoalCompleted/<int:goal_id>', set_goal_completed, name='set_goal_completed'),
]