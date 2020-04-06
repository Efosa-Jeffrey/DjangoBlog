from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    content = models.TextField()
    date = models.CharField(max_length=30)
    image = models.FileField(upload_to="photos")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name_plural = 'Articles'
        ordering = ('date',)
