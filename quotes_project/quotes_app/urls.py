from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'), #http://127.0.0.1:8000/register/
    path('login/', views.user_login, name='login'),
    path('', views.quotes, name='quotes'),
]