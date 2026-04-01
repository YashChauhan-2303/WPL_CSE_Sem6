from django.core.management.base import BaseCommand
from humanapp.models import Human


class Command(BaseCommand):
    help = 'Load sample data into the Human table'

    def handle(self, *args, **options):
        # Clear existing data
        Human.objects.all().delete()
        
        # Create sample data
        sample_data = [
            {
                'first_name': 'John',
                'last_name': 'Doe',
                'phone': '555-1234',
                'address': '123 Main St',
                'city': 'New York'
            },
            {
                'first_name': 'Jane',
                'last_name': 'Smith',
                'phone': '555-5678',
                'address': '456 Oak Ave',
                'city': 'Los Angeles'
            },
            {
                'first_name': 'Bob',
                'last_name': 'Johnson',
                'phone': '555-9012',
                'address': '789 Pine Rd',
                'city': 'Chicago'
            },
            {
                'first_name': 'Alice',
                'last_name': 'Williams',
                'phone': '555-3456',
                'address': '321 Elm St',
                'city': 'Houston'
            },
            {
                'first_name': 'Charlie',
                'last_name': 'Brown',
                'phone': '555-7890',
                'address': '654 Maple Dr',
                'city': 'Phoenix'
            },
        ]
        
        for data in sample_data:
            Human.objects.create(**data)
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded 5 sample records'))
