from django.core.management.base import BaseCommand
from blog.models import News, Category
from django.utils import timezone
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Creates sample articles for testing the home page'

    def handle(self, *args, **kwargs):
        # Get or create categories
        transfer_news, _ = Category.objects.get_or_create(
            name="Transfer News",
            defaults={'slug': 'transfer-news', 'description': 'Latest transfer updates'}
        )
        
        match_analysis, _ = Category.objects.get_or_create(
            name="Match Analysis",
            defaults={'slug': 'match-analysis', 'description': 'In-depth match analysis'}
        )
        
        player_focus, _ = Category.objects.get_or_create(
            name="Player Focus",
            defaults={'slug': 'player-focus', 'description': 'Player spotlight articles'}
        )

        # Sample articles data
        sample_articles = [
            {
                'title': 'Premier League Transfer Window: Biggest Moves and Surprises',
                'content': 'The summer transfer window brings exciting moves across the Premier League. From record-breaking signings to unexpected departures, we analyze the biggest stories shaping the upcoming season. Manchester City has made significant investments in their squad, while Arsenal continues to strengthen their midfield. The competition for top talent has never been fiercer.',
                'excerpt': 'The summer transfer window brings exciting moves across the Premier League. From record-breaking signings to unexpected departures, we analyze the biggest stories shaping the upcoming season.',
                'league': 'premier_league',
                'category': transfer_news,
                'author': 'Transfer Expert',
                'status': 'published'
            },
            {
                'title': 'Bayer Leverkusen\'s Title Defense: Can They Repeat the Magic?',
                'content': 'After their historic Bundesliga triumph, Bayer Leverkusen faces the challenge of defending their title. With key players staying and strategic reinforcements, can they maintain their dominance? The team\'s chemistry and tactical approach will be crucial in the upcoming season.',
                'excerpt': 'After their historic Bundesliga triumph, Bayer Leverkusen faces the challenge of defending their title. With key players staying and strategic reinforcements, can they maintain their dominance?',
                'league': 'bundesliga',
                'category': match_analysis,
                'author': 'FootballDaily Team',
                'status': 'published'
            },
            {
                'title': 'Barça\'s Next No.9: Why Jonathan David Fits the Summer Plan',
                'content': 'Barcelona\'s search for a new striker continues, and Jonathan David emerges as a perfect fit for their summer transfer strategy. The Canadian forward\'s versatility and goal-scoring ability make him an ideal candidate. His work rate and technical skills align perfectly with Barcelona\'s playing style.',
                'excerpt': 'Barcelona\'s search for a new striker continues, and Jonathan David emerges as a perfect fit for their summer transfer strategy. The Canadian forward\'s versatility and goal-scoring ability make him an ideal candidate.',
                'league': 'la_liga',
                'category': transfer_news,
                'author': 'Cherishbakshishar',
                'status': 'published'
            },
            {
                'title': 'Serie A Rising Stars: Young Talents to Watch This Season',
                'content': 'Serie A continues to be a breeding ground for exceptional young talent. This season promises to showcase several rising stars who could make a significant impact. From midfield maestros to defensive stalwarts, Italian football\'s future looks bright.',
                'excerpt': 'Serie A continues to be a breeding ground for exceptional young talent. This season promises to showcase several rising stars who could make a significant impact.',
                'league': 'serie_a',
                'category': player_focus,
                'author': 'Serie A Insider',
                'status': 'published'
            },
            {
                'title': 'PSG\'s New Era: Building for European Success',
                'content': 'Paris Saint-Germain enters a new chapter with fresh leadership and strategic planning. The focus is now on building a team capable of conquering Europe while maintaining domestic dominance. The club\'s approach to player development and tactical evolution will be key to their success.',
                'excerpt': 'Paris Saint-Germain enters a new chapter with fresh leadership and strategic planning. The focus is now on building a team capable of conquering Europe while maintaining domestic dominance.',
                'league': 'ligue_1',
                'category': match_analysis,
                'author': 'Ligue 1 Expert',
                'status': 'published'
            }
        ]

        created_count = 0
        for article_data in sample_articles:
            # Create slug from title
            slug = slugify(article_data['title'])
            
            # Check if article already exists
            if not News.objects.filter(slug=slug).exists():
                News.objects.create(
                    title=article_data['title'],
                    slug=slug,
                    content=article_data['content'],
                    excerpt=article_data['excerpt'],
                    category=article_data['category'],
                    league=article_data['league'],
                    author=article_data['author'],
                    status=article_data['status'],
                    published_at=timezone.now()
                )
                self.stdout.write(self.style.SUCCESS(f'Created article: {article_data["title"]}'))
                created_count += 1
            else:
                self.stdout.write(self.style.WARNING(f'Article already exists: {article_data["title"]}'))

        if created_count > 0:
            self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} sample articles!'))
        else:
            self.stdout.write(self.style.INFO('No new articles were created as they already exist.'))
