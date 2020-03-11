from django.urls import path
from . import views



urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('details/<int:pk>', views.DetailsPage.as_view(), name='details'),
    path('articles/', views.ArticlesPage.as_view(),name='articles'),
]

