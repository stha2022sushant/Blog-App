from django.urls import path 
from . import views


urlpatterns = [
    # for django rest api
    path('', views.getBlogs),
    path('get-blogs-partial/<str:pk>/', views.getBlogsPartial),
    path('add/', views.addBlogs),
    path('update/<str:pk>/', views.updateBlogs),
    path('delete/<str:pk>/', views.deleteBlogs),
    
]