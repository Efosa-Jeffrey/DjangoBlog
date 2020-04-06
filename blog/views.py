from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Article
from .forms import PostForm
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView
)
from django.views.generic.edit import (
    CreateView,
    UpdateView
)


class HomePage(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    paginate_by = 5


class AboutPage(TemplateView):
    template_name = 'blog/about.html'


class DetailsPage(DetailView):
    model = Article
    template_name = 'blog/details.html'
    context_object_name = 'article_list'


class ArticlesPage(ListView):
    model = Article
    template_name = 'blog/articles.html'
    context_object_name = 'article_list'
    paginate_by = 5


class CreatePost(CreateView):
    model = Article
    form_class = PostForm
    template_name = 'blog/new_post.html'
    success_url = reverse_lazy('home')

class UpdatePost(UpdateView):
    model = Article
    template_name = 'blog/update_post.html'
    fields = ['title', 'slug', 'description', 'content']
