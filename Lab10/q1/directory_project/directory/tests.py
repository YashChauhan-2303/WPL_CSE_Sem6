from django.test import TestCase
from .models import Category, Page


class CategoryModelTest(TestCase):
    """Test Category model"""
    
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', visits=10, likes=5)
    
    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Test Category')
        self.assertEqual(self.category.visits, 10)
        self.assertEqual(self.category.likes, 5)
    
    def test_category_str(self):
        self.assertEqual(str(self.category), 'Test Category')


class PageModelTest(TestCase):
    """Test Page model"""
    
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.page = Page.objects.create(
            category=self.category,
            title='Test Page',
            url='https://example.com',
            views=20
        )
    
    def test_page_creation(self):
        self.assertEqual(self.page.title, 'Test Page')
        self.assertEqual(self.page.url, 'https://example.com')
        self.assertEqual(self.page.views, 20)
        self.assertEqual(self.page.category.name, 'Test Category')
