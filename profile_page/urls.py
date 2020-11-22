from django.urls import path, re_path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>/', login_required(views.ProfileView.as_view()), name='profile'),
]