from django.views.generic import ListView, DetailView
from .models import Post  # импортируем Post, а не Article

class NewsList(ListView):
    model = Post
    template_name = 'news/news_list.html'  # путь к шаблону
    context_object_name = 'news_list'
    ordering = ['-created_at']  # сортируем по дате создания, от новых к старым

    def get_queryset(self):
        # Фильтруем только новости (post_type == 'NW')
        return Post.objects.filter(post_type='NW').order_by('-created_at')

class NewsDetail(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'article'
