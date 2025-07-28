from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # Укажите поля точно так же, как в вашей модели
        fields = ['title', 'text', 'author', 'created_at', 'categories']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
            'categories': forms.CheckboxSelectMultiple(),
        }
