from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'categories']  # Уберите 'created_at'
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
        }
