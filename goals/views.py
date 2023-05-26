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
