from django.db import models
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self) -> str:
        return self.name  # type: ignore[return-value]


class News(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('breaking', 'Breaking News'),
    ]
    
    LEAGUE_CHOICES = [
        ('premier_league', 'Premier League'),
        ('serie_a', 'Serie A'),
        ('bundesliga', 'Bundesliga'),
        ('ligue_1', 'Ligue 1'),
        ('la_liga', 'La Liga'),
        ('mls', 'MLS'),
        ('super_lig', 'Süper Lig'),
        ('efl', 'EFL'),
        ('general', 'General'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=300, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news')
    league = models.CharField(max_length=20, choices=LEAGUE_CHOICES, default='general')
    author = models.CharField(max_length=100, default='Football Daily Team')
    featured_image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)  # type: ignore[arg-type]
    is_live = models.BooleanField(default=False)  # type: ignore[arg-type]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = "News"
        ordering = ['-published_at']
    
    def __str__(self) -> str:
        return self.title  # type: ignore[return-value]
    
    def get_absolute_url(self):
        return reverse('blog:news_detail', kwargs={'news_id': self.id})


class MatchPreview(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('upcoming', 'Upcoming'),
    ]
    
    LEAGUE_CHOICES = [
        ('premier_league', 'Premier League'),
        ('serie_a', 'Serie A'),
        ('bundesliga', 'Bundesliga'),
        ('ligue_1', 'Ligue 1'),
        ('la_liga', 'La Liga'),
        ('mls', 'MLS'),
        ('super_lig', 'Süper Lig'),
        ('efl', 'EFL'),
        ('champions_league', 'Champions League'),
        ('europa_league', 'Europa League'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    match_date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    league = models.CharField(max_length=20, choices=LEAGUE_CHOICES)
    
    # Content sections
    introduction = models.TextField()
    home_team_form = models.TextField()
    away_team_form = models.TextField()
    injury_news = models.TextField()
    tactical_preview = models.TextField()
    predicted_lineups = models.TextField()
    prediction = models.CharField(max_length=100)
    
    # Meta
    author = models.CharField(max_length=100, default='Football Daily Team')
    featured_image = models.ImageField(upload_to='match_previews/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)  # type: ignore[arg-type]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = "Match Preview"
        verbose_name_plural = "Match Previews"
        ordering = ['-match_date']
    
    def __str__(self) -> str:
        return f"{self.home_team} vs {self.away_team} - {self.get_league_display()}"  # type: ignore[return-value]
    
    def get_absolute_url(self):
        return reverse('blog:match_preview_detail', kwargs={'preview_id': self.id})


class TransferReview(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('rumor', 'Rumor'),
    ]
    
    LEAGUE_CHOICES = [
        ('premier_league', 'Premier League'),
        ('serie_a', 'Serie A'),
        ('bundesliga', 'Bundesliga'),
        ('ligue_1', 'Ligue 1'),
        ('la_liga', 'La Liga'),
        ('mls', 'MLS'),
        ('super_lig', 'Süper Lig'),
        ('efl', 'EFL'),
        ('champions_league', 'Champions League'),
        ('europa_league', 'Europa League'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    player_name = models.CharField(max_length=100)
    from_team = models.CharField(max_length=100)
    to_team = models.CharField(max_length=100)
    transfer_fee = models.CharField(max_length=50, blank=True)
    league = models.CharField(max_length=20, choices=LEAGUE_CHOICES)
    
    # Content sections
    introduction = models.TextField()
    player_background = models.TextField()
    team_fit = models.TextField()
    strengths = models.TextField()
    weaknesses = models.TextField()
    value_for_money = models.TextField()
    final_verdict = models.TextField()
    
    # Meta
    author = models.CharField(max_length=100, default='Football Daily Team')
    featured_image = models.ImageField(upload_to='transfer_news/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)  # type: ignore[arg-type]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = "Transfer News"
        verbose_name_plural = "Transfer News"
        ordering = ['-published_at']
    
    def __str__(self) -> str:
        return f"{self.player_name} - {self.from_team} to {self.to_team}"  # type: ignore[return-value]
    
    def get_absolute_url(self):
        return reverse('blog:transfer_news_detail', kwargs={'news_id': self.id})
