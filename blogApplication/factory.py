from .models import BlogApp
import factory


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta():
        model = BlogApp