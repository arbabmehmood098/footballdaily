from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('about/', views.about, name='about'),
    path('preview/', views.preview, name='preview'),
    path('transfer-news/', views.transfer_news, name='transfer_news'),
    path('premier-league/', views.premier_league, name='premier_league'),
    path('serie-a/', views.serie_a, name='serie_a'),
    path('bundesliga/', views.bundesliga, name='bundesliga'),
    path('ligue-1/', views.ligue_1, name='ligue_1'),
    path('la-liga/', views.la_liga, name='la_liga'),
    path('mls/', views.mls, name='mls'),
    path('super-lig/', views.super_lig, name='super_lig'),
    path('efl/', views.efl, name='efl'),
]
