from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('post-detail/<int:pk>/', views.post_details, name="post-detail"),
    path('post-edit/<int:pk>/', views.post_edit, name="post-edit"),
    path('post-delete/<int:pk>/', views.post_delete, name="post-delete"),
]
