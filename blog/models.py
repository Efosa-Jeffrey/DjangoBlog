from django.db import models
from django.contrib.auth.models import User



class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="photos")
    date = models.CharField(max_length=30)
    writer = models.CharField(max_length=50)
    content = models.TextField()
    tag = models.CharField(max_length=20)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Articles'

    

