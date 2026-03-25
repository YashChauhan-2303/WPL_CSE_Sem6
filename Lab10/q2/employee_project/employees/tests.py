from django.test import TestCase
from .models import Works, Lives


class WorksModelTest(TestCase):
    """Test Works model"""
    
    def setUp(self):
        self.work = Works.objects.create(
            person_name='John Doe',
            company_name='Tech Corp',
            salary=75000.00
        )
    
    def test_works_creation(self):
        self.assertEqual(self.work.person_name, 'John Doe')
        self.assertEqual(self.work.company_name, 'Tech Corp')
        self.assertEqual(float(self.work.salary), 75000.00)


class LivesModelTest(TestCase):
    """Test Lives model"""
    
    def setUp(self):
        self.lives = Lives.objects.create(
            person_name='John Doe',
            street='123 Main Street',
            city='New York'
        )
    
    def test_lives_creation(self):
        self.assertEqual(self.lives.person_name, 'John Doe')
        self.assertEqual(self.lives.city, 'New York')
