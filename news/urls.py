from django.urls import path
from .views import (
    NewsListView, NewsDetailView, NewsSearchView,
    NewsCreateView, ArticleCreateView,
    PostUpdateView, PostDeleteView
)

urlpatterns = [
    # Новости
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/search/', NewsSearchView.as_view(), name='news_search'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/<int:pk>/edit/', PostUpdateView.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', PostDeleteView.as_view(), name='news_delete'),

    # Статьи
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', PostUpdateView.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', PostDeleteView.as_view(), name='article_delete'),
]
