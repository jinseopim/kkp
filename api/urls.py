from .views import RegisterAPI, LoginAPI, ChangePasswordView, UserAPI, ProfileUpdateAPI, ProfileList
from restaurant import views
from django.urls import path, include
from knox import views as knox_views
from summary.views import SummaryListView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('auth/register/', RegisterAPI.as_view(), name='register-api'),
    path('auth/login/', LoginAPI.as_view(), name='login-api'),
    path("auth/user/", UserAPI.as_view(), name='user-api'),
    path("auth/profile/<int:user_pk>/update/", ProfileUpdateAPI.as_view()),
    path('auth/profiles/', ProfileList.as_view(), name='profile-list'),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='logout-api'),
    path('auth/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall-api'),
    path('auth/change-password/', ChangePasswordView.as_view(), name='change-password-api'),
    path('auth/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset-api')),
    path('summary_list/', SummaryListView.as_view(), name='summary'),
    path('index/', views.index, name='index'),
    path('get_rest_list/', views.get_rest_list, name='get_rest_list'),
]