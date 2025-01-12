from strawberry import auto
import strawberry_django
from django.contrib.auth import get_user_model
from .filters import BlogAppFilter
from .orders import BlogAppOrder
from . import models

@strawberry_django.type(
    models.BlogApp,
    filters=BlogAppFilter,
    order=BlogAppOrder,
    pagination=True
)
class BlogApp:
    id: auto
    title: auto
    blog: auto


@strawberry_django.type(get_user_model())
class User:
    id: auto
    username: auto
    password: auto
    email: auto


@strawberry_django.input(models.BlogApp)
class BlogAppInput:
    id: auto
    title: auto
    blog: auto


@strawberry_django.input(get_user_model())
class UserInput:
    username: auto
    password: auto
    email: auto


@strawberry_django.input(models.BlogApp, partial=True)
class BlogAppPartialInput(BlogAppInput):
    pass