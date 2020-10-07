from django.urls import path

from app_news import views

urlpatterns = [
    #TASK: To create  a News Website where anyone can post news, anyone can modify news, delete it.
    path('',views.home, name="home"),
    path('post/',views.post_news, name="post"),
    path('save/',views.save_news, name="save"),
    path('view_news/',views.view_news, name="view_news"),
    path('view_news_one/<int:pk>',views.view_news_one, name="view_news_one"),
    path('update/<int:pk>',views.update_news, name="update"),
    path('delete/<int:pk>',views.delete_news, name="delete"),
]