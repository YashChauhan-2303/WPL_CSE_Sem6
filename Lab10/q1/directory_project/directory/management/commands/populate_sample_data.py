"""
Sample data loader for Web Directory
Run this script to populate the database with sample categories and pages
"""

from django.core.management.base import BaseCommand
from directory.models import Category, Page


class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **options):
        # Clear existing data
        Category.objects.all().delete()
        Page.objects.all().delete()
        
        # Create sample categories
        categories = [
            Category.objects.create(name='Search Engines', visits=150, likes=45),
            Category.objects.create(name='Social Media', visits=200, likes=80),
            Category.objects.create(name='Development Tools', visits=120, likes=60),
            Category.objects.create(name='Learning Platforms', visits=90, likes=35),
            Category.objects.create(name='News & Information', visits=110, likes=40),
        ]
        
        # Create sample pages for each category
        sample_pages = {
            'Search Engines': [
                {'title': 'Google', 'url': 'https://www.google.com', 'views': 500},
                {'title': 'Bing', 'url': 'https://www.bing.com', 'views': 150},
                {'title': 'DuckDuckGo', 'url': 'https://duckduckgo.com', 'views': 80},
            ],
            'Social Media': [
                {'title': 'Facebook', 'url': 'https://www.facebook.com', 'views': 1200},
                {'title': 'Twitter', 'url': 'https://www.twitter.com', 'views': 800},
                {'title': 'LinkedIn', 'url': 'https://www.linkedin.com', 'views': 600},
                {'title': 'Instagram', 'url': 'https://www.instagram.com', 'views': 900},
            ],
            'Development Tools': [
                {'title': 'GitHub', 'url': 'https://github.com', 'views': 750},
                {'title': 'Stack Overflow', 'url': 'https://stackoverflow.com', 'views': 880},
                {'title': 'Visual Studio Code', 'url': 'https://code.visualstudio.com', 'views': 420},
            ],
            'Learning Platforms': [
                {'title': 'Coursera', 'url': 'https://www.coursera.org', 'views': 350},
                {'title': 'Udemy', 'url': 'https://www.udemy.com', 'views': 450},
                {'title': 'Khan Academy', 'url': 'https://www.khanacademy.org', 'views': 280},
            ],
            'News & Information': [
                {'title': 'BBC News', 'url': 'https://www.bbc.com/news', 'views': 200},
                {'title': 'CNN', 'url': 'https://www.cnn.com', 'views': 180},
                {'title': 'Wikipedia', 'url': 'https://www.wikipedia.org', 'views': 920},
            ],
        }
        
        # Add pages to categories
        for category in categories:
            pages = sample_pages.get(category.name, [])
            for page_data in pages:
                Page.objects.create(
                    category=category,
                    title=page_data['title'],
                    url=page_data['url'],
                    views=page_data['views']
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully loaded sample data: '
                f'{len(categories)} categories and '
                f'{sum(len(pages) for pages in sample_pages.values())} pages'
            )
        )
