from django.urls import path
from .views import index, verify, refresh

urlpatterns = [
    path('', index, name='index'),
    path('verify/', verify, name='verify'),
    path('refresh/', refresh, name='refresh'),
]
