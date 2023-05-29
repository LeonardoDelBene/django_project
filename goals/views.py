from django.shortcuts import render, redirect
from .models import Goal


# Create your views here.
def get_all_goals(request):
    if(request.user.is_authenticated):
        if(request.method == 'GET'):
            user=request.user
            goals = Goal.objects.filter(user=user)
            context={
                'goals': goals
            }
            return render(request, 'goals.html', context)
    else :
        return redirect('login')

def create_goals(request):
    if(request.user.is_authenticated):
        if(request.method == 'POST'):
            user=request.user
            goal=request.POST['goal']
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            completed=request.POST['completed']
            Goal.objects.create(user=user, goal=goal, start_date=start_date, end_date=end_date, completed=completed)
            return redirect('profile_home')
        else:
            return render(request, 'create_goals.html')
    else :
        return redirect('login')

def view_completed_goals(request):
    if(request.user.is_authenticated):
        if(request.method == 'GET'):
            user=request.user
            goals = Goal.objects.filter(user=user, completed=True)
            context={
                'goals': goals
            }
            return render(request, 'goals.html', context)

def view_incompleted_goals(request):
    if(request.user.is_authenticated):
        if(request.method == 'GET'):
            user=request.user
            goals = Goal.objects.filter(user=user, completed=False)
            context={
                'goals': goals
            }
            return render(request, 'goals.html', context)

def set_goal_completed(request, goal_id):
    if(request.user.is_authenticated):
        if(request.method == 'GET'):
            goal = Goal.objects.get(id=goal_id)
            goal.completed=True
            goal.save()
            goals=Goal.objects.filter(user=request.user)
            context={
                'goals': goals
            }
            return render(request, 'goals.html', context)