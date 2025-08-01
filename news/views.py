from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django_filters.views import FilterView

from .models import Post
from .filters import PostFilter
from .forms import PostForm


@login_required
@require_POST
def become_author(request):
    group, created = Group.objects.get_or_create(name='authors')
    request.user.groups.add(group)
    return redirect('profile')


class NewsListView(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10
    ordering = ['-created_at']
    filterset = None

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
        queryset = super().get_queryset()
        return queryset.filter(post_type='NW').order_by('-created_at')


class ArticleListView(ListView):
    model = Post
    template_name = 'news/article_list.html'
    context_object_name = 'article_list'
    paginate_by = 10
    ordering = ['-created_at']

    def get_queryset(self):
        return Post.objects.filter(post_type='AR').order_by('-created_at')


class NewsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    raise_exception = True
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('news_list')
    login_url = '/login/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'NW'
        post.save()
        return super().form_valid(form)


class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    raise_exception = True
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('article_list')
    login_url = '/login/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'AR'
        post.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    raise_exception = True
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    login_url = '/login/'

    def get_success_url(self):
        if self.object.post_type == 'NW':
            return reverse_lazy('news_list')
        return reverse_lazy('article_list')


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    raise_exception = True
    model = Post
    template_name = 'post_confirm_delete.html'
    login_url = '/login/'

    def get_success_url(self):
        if self.object.post_type == 'NW':
            return reverse_lazy('news_list')
        return reverse_lazy('article_list')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        # Если есть модель профиля, добавить сюда, например
        # context['profile'] = self.request.user.profile
        return context
