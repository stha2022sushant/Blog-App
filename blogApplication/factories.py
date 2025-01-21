import factory
from faker import Faker
from .models import BlogApp
from django.contrib.auth import get_user_model
from random import choice

fake = Faker()
"""
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'password123')

    """

class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BlogApp

    title = factory.Faker('sentence', nb_words=4)  # Random title
    blog = factory.Faker('paragraph', nb_sentences=5)  # Random content
    
    # Use 'author' as either a random User or None (to simulate optional author)
    author = factory.LazyAttribute(lambda _: choice([None, UserFactory()]))  # Randomly choose None or a user

