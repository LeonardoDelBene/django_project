from django.urls import path

from account.views import ProfileHomeView

urlpatterns=[
    path('', ProfileHomeView.as_view(), name='profile_home')
]