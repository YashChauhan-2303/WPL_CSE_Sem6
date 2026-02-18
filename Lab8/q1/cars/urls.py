from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_car, name='select_car'),
    path('display/', views.display_car, name='display_car'),
]
