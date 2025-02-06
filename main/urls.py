from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('create/', views.Create, name='create'),
]
