from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Подключаем приложение news
    path('', include('news.urls')),

    # Подключаем маршруты allauth
    path('accounts/', include('allauth.urls')),
]
