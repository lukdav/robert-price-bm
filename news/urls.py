from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_news, name='news'),
    path('<slug:slug>/', views.news_article, name='news_article'),
    path('add_article/', views.add_post, name='add_post'),
]
