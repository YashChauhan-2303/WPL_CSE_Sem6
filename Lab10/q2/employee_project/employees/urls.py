from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert-works/', views.insert_works, name='insert_works'),
    path('insert-lives/', views.insert_lives, name='insert_lives'),
    path('search-company/', views.search_company, name='search_company'),
    path('view-works/', views.view_all_works, name='view_all_works'),
    path('view-lives/', views.view_all_lives, name='view_all_lives'),
]
