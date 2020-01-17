from django.urls import path
from . import views



urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('details/<int:pk>', views.DetailsPage.as_view(), name='details'),
    
    path('articles/', views.ArticlesPage.as_view(),name='articles'),
    path('articles/page2', views.Page2.as_view(),name='page2'),
    path('articles/page3', views.Page3.as_view(),name='page3'),
    path('articles/page4', views.Page4.as_view(),name='page4'),
    path('articles/page5', views.Page5.as_view(),name='page5'),

]
