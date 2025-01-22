from django.urls import path 
from . import views


urlpatterns = [
    # for django rest api
    path('', views.getData),
]