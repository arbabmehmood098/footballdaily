from django.core.management.base import BaseCommand
from blog.models import Category

class Command(BaseCommand):
    help = 'Create default categories for the blog'

    def handle(self, *args, **options):
        categories = [
            {'name': 'Transfer News', 'slug': 'transfer-news', 'description': 'Latest transfer updates and rumors'},
            {'name': 'Match Analysis', 'slug': 'match-analysis', 'description': 'In-depth match analysis and reviews'},
            {'name': 'Player Focus', 'slug': 'player-focus', 'description': 'Individual player profiles and performances'},
            {'name': 'Team News', 'slug': 'team-news', 'description': 'Team updates and announcements'},
            {'name': 'League Updates', 'slug': 'league-updates', 'description': 'General league news and updates'},
            {'name': 'Breaking News', 'slug': 'breaking-news', 'description': 'Urgent and breaking football news'},
            {'name': 'Opinion', 'slug': 'opinion', 'description': 'Editorial opinions and commentary'},
            {'name': 'History', 'slug': 'history', 'description': 'Football history and memorable moments'},
        ]
        
        created_count = 0
        for cat_data in categories:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={
                    'name': cat_data['name'],
                    'description': cat_data['description']
                }
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created category: {category.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Category already exists: {category.name}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} new categories!')
        )
