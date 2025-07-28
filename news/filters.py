import django_filters
from django import forms
from .models import Post

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Название'
    )

    # Используйте этот фильтр, если у Post.author есть связь с User через author__user
    author = django_filters.CharFilter(
        field_name='author__user__username',
        lookup_expr='icontains',
        label='Автор'
    )

    # Если у вас Post.author — это напрямую User, то вместо author используйте так (раскомментируйте):
    # author = django_filters.CharFilter(
    #     field_name='author__username',
    #     lookup_expr='icontains',
    #     label='Автор'
    # )

    created_at = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='gte',  # включительно — дата "больше или равна"
        label='Дата позже или равна',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Post
        fields = ['title', 'author', 'created_at']
