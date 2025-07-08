from django.contrib.auth.models import User
from news.models import Author, Category, Post, Comment

# Создаем или получаем пользователей
user1, created = User.objects.get_or_create(username='user1')
user2, created = User.objects.get_or_create(username='user2')

# Создаем или получаем авторов
author1, created = Author.objects.get_or_create(user=user1)
author2, created = Author.objects.get_or_create(user=user2)

# Создаем или получаем категории
cat1, created = Category.objects.get_or_create(name='Спорт')
cat2, created = Category.objects.get_or_create(name='Политика')
cat3, created = Category.objects.get_or_create(name='Образование')
cat4, created = Category.objects.get_or_create(name='Наука')

# Создаем или получаем посты
post1, created = Post.objects.get_or_create(author=author1, post_type='AR', title='Статья 1', text='Текст статьи 1')
post2, created = Post.objects.get_or_create(author=author2, post_type='AR', title='Статья 2', text='Текст статьи 2')
news1, created = Post.objects.get_or_create(author=author1, post_type='NE', title='Новость 1', text='Текст новости 1')

# Добавляем категории к постам
post1.categories.add(cat1, cat2)
post2.categories.add(cat3)
news1.categories.add(cat4)

# Создаем комментарии
comment1, created = Comment.objects.get_or_create(post=post1, user=user2, text='Комментарий 1')
comment2, created = Comment.objects.get_or_create(post=post2, user=user1, text='Комментарий 2')
comment3, created = Comment.objects.get_or_create(post=news1, user=user2, text='Комментарий 3')
comment4, created = Comment.objects.get_or_create(post=post1, user=user1, text='Комментарий 4')

# Работа с рейтингами
post1.like()
post2.like()
news1.dislike()
comment1.like()
comment2.dislike()
comment3.like()
comment4.like()

# Обновляем рейтинги авторов
author1.update_rating()
author2.update_rating()

# Выводим лучшего пользователя
best_author = Author.objects.order_by('-rating').first()
print(best_author.user.username, best_author.rating)

# Выводим лучшую статью
best_post = Post.objects.order_by('-rating').first()
print(best_post.created_at, best_post.author.user.username, best_post.rating, best_post.title, best_post.preview())

# Выводим комментарии к лучшей статье
for comment in Comment.objects.filter(post=best_post):
    print(comment.created_at, comment.user.username, comment.rating, comment.text)
