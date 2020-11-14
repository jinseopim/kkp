from django.urls import path
from . import views

urlpatterns = [
    path('profile_list/', views.profile_list, name='profile_list'),
]