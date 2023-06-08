from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, homePage_view

urlpatterns = [
    # ...
    path('', homePage_view, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', register_view, name='register'),
    # ...
]
