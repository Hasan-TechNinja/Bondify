from django.urls import path
from . import views

urlpatterns = [
    path('singup/', views.Registration, name='registration'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
]
