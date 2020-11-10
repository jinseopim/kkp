from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('accounts/register_page/', views.register_page, name='register_page'),
    path('accounts/forgot_password_page/', views.forgot_password_page, name='forgot_password_page'),
]