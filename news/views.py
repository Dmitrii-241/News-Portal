from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from .models import Post
from .filters import PostFilter
from .forms import PostForm

class NewsListView(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10
    ordering = ['-created_at']

    filterset = None  # для IDE

    def get_queryset(self):
        queryset = Post.objects.filter(post_type='NW').order_by('-created_at')
        self.filterset = PostFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class NewsDetailView(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'article'

class NewsSearchView(FilterView):
    filterset_class = PostFilter
    template_name = 'news/news_search.html'
    context_object_name = 'news_list'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(post_type='NW').order_by('-created_at')


# Создание новостей
class NewsCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'NW'  # тип новости в модели — 'NW'
        post.save()
        return super().form_valid(form)

# Создание статей
class ArticleCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('article_list')  # создайте этот URL в urls.py

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'AR'  # тип статьи в модели — 'AR'
        post.save()
        return super().form_valid(form)

# Редактирование поста (как новости, так и статьи)
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'

    def get_success_url(self):
        if self.object.post_type == 'NW':
            return reverse_lazy('news_list')
        return reverse_lazy('article_list')

# Удаление поста
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'

    def get_success_url(self):
        if self.object.post_type == 'NW':
            return reverse_lazy('news_list')
        return reverse_lazy('article_list')
