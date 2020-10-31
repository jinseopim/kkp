# api/urls.py
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserAPIView, LogoutUserAPIView
from django.urls import path, include
from .views import HelloAPI

urlpatterns = [
    path("hello/", HelloAPI),
    url(r'^auth/login/$',
        obtain_auth_token,
        name='auth_user_login'),
    url(r'^auth/register/$',
        CreateUserAPIView.as_view(),
        name='auth_user_create'),
    url(r'^auth/logout/$',
        LogoutUserAPIView.as_view(),
        name='auth_user_logout')
]