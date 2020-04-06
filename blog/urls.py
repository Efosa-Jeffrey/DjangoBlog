from django.urls import path
from blog import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('<slug:slug>', views.DetailsPage.as_view(), name='details'),
    path('articles/', views.ArticlesPage.as_view(), name='articles'),
    path('new/', views.CreatePost.as_view(), name='create_post'),
    path('<slug:slug>/update', views.UpdatePost.as_view(), name='update_post'),
    path('<slug:slug>/delete', views.DeletePost.as_view(), name='delete_post')
]
