from django import forms
from .models import Category, Page


class CategoryForm(forms.ModelForm):
    """Form for creating and updating categories"""
    
    class Meta:
        model = Category
        fields = ['name', 'visits', 'likes']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name',
                'required': True
            }),
            'visits': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of visits',
                'min': '0'
            }),
            'likes': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of likes',
                'min': '0'
            }),
        }


class PageForm(forms.ModelForm):
    """Form for creating and updating pages"""
    
    class Meta:
        model = Page
        fields = ['category', 'title', 'url', 'views']
        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter page title',
                'required': True
            }),
            'url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com',
                'required': True
            }),
            'views': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of views',
                'min': '0'
            }),
        }
