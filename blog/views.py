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


class AboutPage(TemplateView):
    template_name = 'blog/about.html'


class DetailsPage(DetailView):
    model = Article
    template_name = 'blog/details.html'
    context_object_name = 'article_list'




# article home/page1
class ArticlesPage(ListView):
    model = Article
    template_name = 'blog/articles/page1.html'
    context_object_name = 'article_list'

# article page2
class Page2(ListView):
    model = Article
    template_name = 'blog/articles/page2.html'
    context_object_name = 'article_list'

# article page3
class Page3(ListView):
    model = Article
    template_name = 'blog/articles/page3.html'
    context_object_name = 'article_list'


# article page4
class Page4(ListView):
    model = Article
    template_name = 'blog/articles/page4.html'
    context_object_name = 'article_list'


# article page5
class Page5(ListView):
    model = Article
    template_name = 'blog/articles/page5.html'
    context_object_name = 'article_list'
    



