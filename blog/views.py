from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .models import News, Category, MatchPreview, TransferReview

def home(request):
    """Home page with featured news and latest updates"""
    featured_news = News.objects.filter(is_featured=True, status='published')[:3]
    latest_news = News.objects.filter(status='published')[:6]
    breaking_news = News.objects.filter(status='breaking')[:2]
    
    context = {
        'featured_news': featured_news,
        'latest_news': latest_news,
        'breaking_news': breaking_news,
    }
    return render(request, 'blog/home.html', context)

def news_list(request):
    """List all published news with pagination"""
    news_list = News.objects.filter(status='published')
    paginator = Paginator(news_list, 10)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    
    context = {
        'news': news,
    }
    return render(request, 'blog/news_list.html', context)

def news_detail(request, news_id):
    """Detail view for individual news article"""
    news = get_object_or_404(News, id=news_id, status='published')
    related_news = News.objects.filter(
        category=news.category, 
        status='published'
    ).exclude(id=news_id)[:3]
    
    context = {
        'news': news,
        'related_news': related_news,
    }
    return render(request, 'blog/news_detail.html', context)


def about(request):
    """About page"""
    return render(request, 'blog/about.html')

def preview(request):
    """Match Previews page - organized by league"""
    match_previews = MatchPreview.objects.filter(status='published').order_by('league', '-match_date')
    
    # Group match previews by league
    leagues_previews = {}
    for preview in match_previews:
        league = preview.get_league_display()
        if league not in leagues_previews:
            leagues_previews[league] = []
        leagues_previews[league].append(preview)
    
    context = {
        'leagues_previews': leagues_previews,
        'match_previews': match_previews,
    }
    return render(request, 'blog/preview.html', context)

def transfer_news(request):
    """Transfer News page - organized by league"""
    transfer_news = TransferReview.objects.filter(status='published').order_by('league', '-published_at')
    
    # Group transfer news by league
    leagues_transfers = {}
    for news in transfer_news:
        league = news.get_league_display()
        if league not in leagues_transfers:
            leagues_transfers[league] = []
        leagues_transfers[league].append(news)
    
    context = {
        'leagues_transfers': leagues_transfers,
        'transfer_news': transfer_news,
    }
    return render(request, 'blog/transfer-news.html', context)

def premier_league(request):
    """Premier League page"""
    league_news = News.objects.filter(league='premier_league', status='published')
    paginator = Paginator(league_news, 5)  # Show 5 blogs per page
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    
    context = {
        'league_name': 'Premier League',
        'league_description': 'The Premier League is the top level of the English football league system.',
        'news': news,
        'league_slug': 'premier_league',
    }
    return render(request, 'blog/league.html', context)

def serie_a(request):
    """Serie A page"""
    league_news = News.objects.filter(league='serie_a', status='published')
    paginator = Paginator(league_news, 5)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    
    context = {
        'league_name': 'Serie A',
        'league_description': 'Serie A is the top professional football league in Italy.',
        'news': news,
        'league_slug': 'serie_a',
    }
    return render(request, 'blog/league.html', context)

def bundesliga(request):
    """Bundesliga page"""
    league_news = News.objects.filter(league='bundesliga', status='published')
    paginator = Paginator(league_news, 5)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    
    context = {
        'league_name': 'Bundesliga',
        'league_description': 'The Bundesliga is the top professional football league in Germany.',
        'news': news,
        'league_slug': 'bundesliga',
    }
    return render(request, 'blog/league.html', context)

def ligue_1(request):
    """Ligue 1 page"""
    league_news = News.objects.filter(league='ligue_1', status='published')
    paginator = Paginator(league_news, 5)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    
    context = {
        'league_name': 'Ligue 1',
        'league_description': 'Ligue 1 is the top professional football league in France.',
        'news': news,
        'league_slug': 'ligue_1',
    }
    return render(request, 'blog/league.html', context)

def la_liga(request):
    """La Liga page"""
    league_news = News.objects.filter(league='la_liga', status='published')
    paginator = Paginator(league_news, 5)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    
    context = {
        'league_name': 'La Liga',
        'league_description': 'La Liga is the top professional football league in Spain.',
        'news': news,
        'league_slug': 'la_liga',
    }
    return render(request, 'blog/league.html', context)

def mls(request):
    """MLS page"""
    league_news = News.objects.filter(league='mls', status='published')
    paginator = Paginator(league_news, 5)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    
    context = {
        'league_name': 'MLS',
        'league_description': 'Major League Soccer is the top professional football league in the United States and Canada.',
        'news': news,
        'league_slug': 'mls',
    }
    return render(request, 'blog/league.html', context)

def super_lig(request):
    """Süper Lig page"""
    league_news = News.objects.filter(league='super_lig', status='published')
    paginator = Paginator(league_news, 5)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    
    context = {
        'league_name': 'Süper Lig',
        'league_description': 'The Süper Lig is the top professional football league in Turkey.',
        'news': news,
        'league_slug': 'super_lig',
    }
    return render(request, 'blog/league.html', context)

def efl(request):
    """EFL page"""
    league_news = News.objects.filter(league='efl', status='published')
    paginator = Paginator(league_news, 5)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    
    context = {
        'league_name': 'EFL',
        'league_description': 'The English Football League (EFL) is the second tier of English football, featuring the Championship, League One, and League Two.',
        'news': news,
        'league_slug': 'efl',
    }
    return render(request, 'blog/league.html', context)