from django.contrib.auth import get_user_model
from .models import BlogApp
from factory.django import DjangoModelFactory 

class BlogFactory(DjangoModelFactory):
    class Meta():
        model = BlogApp
    
