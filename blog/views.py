from django.shortcuts import render
from .models import Article

from django.views.generic import (
    ListView,
    DetailView,
    TemplateView
)

class HomePage(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    paginate_by = 3


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


