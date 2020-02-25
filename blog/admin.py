from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'writer')


admin.site.register(Article, ArticleAdmin)
