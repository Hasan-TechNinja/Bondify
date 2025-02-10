from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('create/', views.Create, name='create'),
    path('update/', views.Update, name='update'),
    path('update/<int:pk>', views.Update, name='update'),
]
