from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<url>/', views.blog_detail, name='blog_detail'),
    path('category/<category_name>/', views.blog_category, name='blog_category'),
]