from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('login'))
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def homePage_view(request):
    return render(request, '../templates/index.html')
