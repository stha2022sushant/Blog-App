from typing import Optional
from strawberry import auto
import strawberry_django
from django.db.models import Q
from . import models

@strawberry_django.filters.filter(models.BlogApp, lookups=True)
class BlogAppFilter:
    id: auto
    title: auto

    @strawberry_django.filter_field
    def special_filters(self, prefix: str, value: str):
        return Q(**{f"{prefix}name": value})