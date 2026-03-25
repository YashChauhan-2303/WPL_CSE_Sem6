from django.urls import path
from . import views

urlpatterns = [
    path('', views.institute_list, name='institute_list'),
]
