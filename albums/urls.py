from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('post/<int:pk>/', views.album_detail, name='album_detail'),
    path('post/new/', views.album_new, name='album_new'),
    path('post/<int:pk>/edit/', views.album_edit, name='album_edit'),
]