from .views import RegisterAPI, LoginAPI, ChangePasswordView
from restaurant import views
from django.urls import path, include
from knox import views as knox_views
from summary.views import SummaryListView

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('summary_list/', SummaryListView.as_view(), name='summary'),
    path('index/', views.index, name='summary'),
    path('get_rest_list/', views.get_rest_list, name='summary'),
]
