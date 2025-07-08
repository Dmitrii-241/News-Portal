from django.urls import path
from .views import NewsList, NewsDetail

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),           # Список новостей по адресу /news/
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),  # Детальная новость по адресу /news/<id>/
]
