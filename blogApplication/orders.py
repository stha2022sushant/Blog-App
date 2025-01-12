from strawberry import auto
import strawberry_django
from . import models

@strawberry_django.ordering.order(models.BlogApp)
class BlogAppOrder:
    title: auto
    blog: auto