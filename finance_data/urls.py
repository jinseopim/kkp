from django.urls import path
from . import views

urlpatterns = [
    path('get_finance_data/', views.get_finance_data, name='get_finance_data'),
]