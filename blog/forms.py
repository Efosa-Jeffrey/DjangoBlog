from django import forms
from blog.models import Article

class PostForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['author', 'title', 'slug', 'description', 'content', 'date', 'image']
