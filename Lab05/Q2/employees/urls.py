from django.urls import path
from .views import index, check_eligibility

urlpatterns = [
    path('', index, name='index'),
    path('check/', check_eligibility, name='check_eligibility'),
]
