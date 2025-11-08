from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.admin import AdminSite
from django.contrib.admin.apps import AdminConfig
from django.core.exceptions import ValidationError
from django.template.response import TemplateResponse
from typing import Any
from .models import News, Category, MatchPreview, TransferReview
from .forms import NewsForm, CategoryForm

# Customize the main admin site
admin.site.site_header = 'Football Daily Administration'
admin.site.site_title = 'Football Daily Admin'
admin.site.index_title = 'Football Daily Administration'

# Create a custom admin app configuration
class LeagueAdminAppConfig(AdminConfig):
    default_site = 'blog.admin.LeagueAdminSite'

# Create custom admin site
class LeagueAdminSite(AdminSite):
    site_header = 'Football Daily Administration'
    site_title = 'Football Daily Admin'
    index_title = 'Football Daily Administration'
    
    def login(self, request, extra_context=None):
        """Custom login view to ensure proper authentication"""
        return super().login(request, extra_context)
    
    def logout(self, request, extra_context=None):
        """Custom logout view to ensure proper logout"""
        from django.contrib.auth import logout
        from django.shortcuts import redirect
        logout(request)
        return redirect('/admin/login/')
    
    def index(self, request: Any, extra_context: Any = None) -> TemplateResponse:
        """
        Display the main admin index page with league shortcuts.
        """
        context = {
            'title': self.index_title,
            'app_list': [],  # Empty app list to avoid reverse URL issues
            'log_entries': [],  # Empty log entries to avoid template errors
            'has_permission': True,
            'site_url': '/',
            'league_links': [
                {
                    'name': 'Premier League',
                    'url': '/admin/blog/news/premier-league/',
                    'icon': '🏴󠁧󠁢󠁥󠁮󠁧󠁿',
                    'description': 'Manage Premier League blogs and news'
                },
                {
                    'name': 'Serie A',
                    'url': '/admin/blog/news/serie-a/',
                    'icon': '🇮🇹',
                    'description': 'Manage Serie A blogs and news'
                },
                {
                    'name': 'Bundesliga',
                    'url': '/admin/blog/news/bundesliga/',
                    'icon': '🇩🇪',
                    'description': 'Manage Bundesliga blogs and news'
                },
                {
                    'name': 'Ligue 1',
                    'url': '/admin/blog/news/ligue-1/',
                    'icon': '🇫🇷',
                    'description': 'Manage Ligue 1 blogs and news'
                },
                {
                    'name': 'La Liga',
                    'url': '/admin/blog/news/la-liga/',
                    'icon': '🇪🇸',
                    'description': 'Manage La Liga blogs and news'
                },
                {
                    'name': 'MLS',
                    'url': '/admin/blog/news/mls/',
                    'icon': '🇺🇸',
                    'description': 'Manage MLS blogs and news'
                },
                {
                    'name': 'Süper Lig',
                    'url': '/admin/blog/news/super-lig/',
                    'icon': '🇹🇷',
                    'description': 'Manage Süper Lig blogs and news'
                },
                {
                    'name': 'EFL',
                    'url': '/admin/blog/news/efl/',
                    'icon': '🏴󠁧󠁢󠁥󠁮󠁧󠁿',
                    'description': 'Manage EFL blogs and news'
                },
            ]
        }
        context.update(extra_context or {})
        return TemplateResponse(request, 'admin/league_index.html', context)


class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    list_display = ['title', 'league', 'category', 'author', 'status', 'is_featured', 'is_live', 'published_at']
    list_filter = ['status', 'league', 'is_featured', 'is_live', 'category', 'published_at']
    search_fields = ['title', 'content', 'author']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    ordering = ['-published_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'content', 'excerpt', 'category', 'league', 'author')
        }),
        ('Media', {
            'fields': ('featured_image',),
            'description': 'Upload an image (max 2MB). Supported formats: JPEG, PNG, GIF, WebP'
        }),
        ('Publishing', {
            'fields': ('status', 'is_featured', 'is_live', 'published_at')
        }),
    )
    
    def save_model(self, request, obj, form, change):
        """Override save to handle file size validation"""
        try:
            super().save_model(request, obj, form, change)
        except ValidationError as e:
            messages.error(request, str(e))
            return
    
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('premier-league/', self.admin_site.admin_view(self.premier_league_view), name='blog_news_premier_league'),
            path('serie-a/', self.admin_site.admin_view(self.serie_a_view), name='blog_news_serie_a'),
            path('bundesliga/', self.admin_site.admin_view(self.bundesliga_view), name='blog_news_bundesliga'),
            path('ligue-1/', self.admin_site.admin_view(self.ligue_1_view), name='blog_news_ligue_1'),
            path('la-liga/', self.admin_site.admin_view(self.la_liga_view), name='blog_news_la_liga'),
            path('mls/', self.admin_site.admin_view(self.mls_view), name='blog_news_mls'),
            path('super-lig/', self.admin_site.admin_view(self.super_lig_view), name='blog_news_super_lig'),
            path('efl/', self.admin_site.admin_view(self.efl_view), name='blog_news_efl'),
        ]
        return custom_urls + urls
    
    def premier_league_view(self, request):
        return self.league_admin_view(request, 'premier_league', 'Premier League')
    
    def serie_a_view(self, request):
        return self.league_admin_view(request, 'serie_a', 'Serie A')
    
    def bundesliga_view(self, request):
        return self.league_admin_view(request, 'bundesliga', 'Bundesliga')
    
    def ligue_1_view(self, request):
        return self.league_admin_view(request, 'ligue_1', 'Ligue 1')
    
    def la_liga_view(self, request):
        return self.league_admin_view(request, 'la_liga', 'La Liga')
    
    def mls_view(self, request):
        return self.league_admin_view(request, 'mls', 'MLS')
    
    def super_lig_view(self, request):
        return self.league_admin_view(request, 'super_lig', 'Süper Lig')
    
    def efl_view(self, request):
        return self.league_admin_view(request, 'efl', 'EFL')
    
    def league_admin_view(self, request, league_slug, league_name):
        if request.method == 'POST':
            # Handle form submission
            title = request.POST.get('title')
            content = request.POST.get('content')
            excerpt = request.POST.get('excerpt', '')
            author = request.POST.get('author', 'Football Daily Team')
            category_id = request.POST.get('category')
            
            if title and content and category_id:
                try:
                    category = Category.objects.get(id=category_id)  # type: ignore
                    news = News.objects.create(  # type: ignore
                        title=title,
                        slug=title.lower().replace(' ', '-').replace(':', '').replace(',', ''),
                        content=content,
                        excerpt=excerpt,
                        category=category,
                        league=league_slug,
                        author=author,
                        status='published'
                    )
                    
                    # Handle featured image upload with size validation
                    if 'featured_image' in request.FILES:
                        image = request.FILES['featured_image']
                        max_size = 2 * 1024 * 1024  # 2MB
                        
                        if image.size > max_size:
                            messages.error(request, f'Image size should not exceed 2MB. Current size: {image.size / (1024 * 1024):.2f}MB')
                            return redirect(request.path)
                        
                        # Check file type
                        allowed_types = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/webp']
                        if image.content_type not in allowed_types:
                            messages.error(request, 'Only JPEG, PNG, GIF, and WebP images are allowed.')
                            return redirect(request.path)
                        
                        news.featured_image = image
                        news.save()
                    messages.success(request, f'Blog post "{title}" has been created successfully for {league_name}!')
                    return redirect(f'/admin/blog/news/{news.id}/change/')
                except Exception as e:
                    messages.error(request, f'Error creating blog post: {str(e)}')
            else:
                messages.error(request, 'Please fill in all required fields.')
        
        # Get existing blogs for this league
        league_news = News.objects.filter(league=league_slug).order_by('-published_at')  # pyright: ignore
        categories = Category.objects.all()  # pyright: ignore
        
        context = {
            'league_name': league_name,
            'league_slug': league_slug,
            'league_news': league_news,
            'categories': categories,
            'title': f'Manage {league_name} Blogs',
            'opts': self.model._meta,
            'has_view_permission': True,
        }
        
        return render(request, 'admin/blog/news/league_admin.html', context)


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']

# Match Preview Admin
class MatchPreviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'home_team', 'away_team', 'match_date', 'league', 'status', 'is_featured']
    list_filter = ['league', 'status', 'is_featured', 'match_date']
    search_fields = ['title', 'home_team', 'away_team', 'venue']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'match_date'
    ordering = ['-match_date']
    
    fieldsets = (
        ('Match Details', {
            'fields': ('title', 'slug', 'home_team', 'away_team', 'match_date', 'venue', 'league')
        }),
        ('Content', {
            'fields': ('introduction', 'home_team_form', 'away_team_form', 'injury_news', 'tactical_preview', 'predicted_lineups', 'prediction')
        }),
        ('Meta', {
            'fields': ('author', 'featured_image', 'status', 'is_featured')
        }),
    )

# Transfer News Admin
class TransferNewsAdmin(admin.ModelAdmin):
    list_display = ['player_name', 'from_team', 'to_team', 'transfer_fee', 'league', 'status', 'is_featured']
    list_filter = ['league', 'status', 'is_featured', 'published_at']
    search_fields = ['player_name', 'from_team', 'to_team', 'title']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    ordering = ['-published_at']
    
    fieldsets = (
        ('Transfer Details', {
            'fields': ('title', 'slug', 'player_name', 'from_team', 'to_team', 'transfer_fee', 'league')
        }),
        ('Content', {
            'fields': ('introduction', 'player_background', 'team_fit', 'strengths', 'weaknesses', 'value_for_money', 'final_verdict')
        }),
        ('Meta', {
            'fields': ('author', 'featured_image', 'status', 'is_featured')
        }),
    )

# Register models with the default admin site
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MatchPreview, MatchPreviewAdmin)
admin.site.register(TransferReview, TransferNewsAdmin)
