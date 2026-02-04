from django.urls import path
from .views import index, submit_data

urlpatterns = [
    path('', index, name='index'),
    path('submit/', submit_data, name='submit'),
]
