from django.contrib import admin
from .models import Category, Page


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'visits', 'likes', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']
    ordering = ['-created_at']


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'views', 'created_at']
    search_fields = ['title', 'category__name']
    list_filter = ['category', 'created_at']
    ordering = ['-created_at']
