from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.index, name='index'),
    
    # Category URLs
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category/<int:pk>/like/', views.like_category, name='like_category'),
    path('category/new/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    
    # Page URLs
    path('pages/', views.PageListView.as_view(), name='page_list'),
    path('page/<int:pk>/', views.PageDetailView.as_view(), name='page_detail'),
    path('page/new/', views.PageCreateView.as_view(), name='page_create'),
    path('page/<int:pk>/edit/', views.PageUpdateView.as_view(), name='page_update'),
    path('page/<int:pk>/delete/', views.PageDeleteView.as_view(), name='page_delete'),
]
