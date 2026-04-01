from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.update_human, name='update'),
    path('delete/', views.delete_human, name='delete'),
        path('add/', views.add_human, name='add'),
]
