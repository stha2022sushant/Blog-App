from typing import Optional

from strawberry import auto

import strawberry_django
from django.contrib.auth import get_user_model
from django.db.models import Q

from . import models

# filters
    
@strawberry_django.filters.filter(models.BlogApp, lookups=True)
class BlogAppFilter:
    id: auto
    title: auto
    #blog: Optional["BlogAppFilter"]

    @strawberry_django.filter_field
    def special_filters(self, prefix: str, value: str):
        return Q(**{f"{prefix}name": value})
    


# order

@strawberry_django.ordering.order(models.BlogApp)
class BlogAppOrder:
    title: auto
    blog: auto
    
    



# types

@strawberry_django.type(
    models.BlogApp, 
    filters=BlogAppFilter,
    order= BlogAppOrder,
    pagination= True)
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


# input types

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


# partial input types

@strawberry_django.input(models.BlogApp, partial=True)
class BlogAppPartialInput(BlogAppInput):
    pass