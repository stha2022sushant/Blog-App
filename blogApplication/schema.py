import strawberry

import strawberry_django
from strawberry_django import auth, mutations

from .types import (
    BlogApp,
    BlogAppInput, 
    BlogAppPartialInput,
    User,
    UserInput,
)


@strawberry.type
class Query:
    blog: BlogApp = strawberry_django.field()
    blogs: list[BlogApp] = strawberry_django.field()



@strawberry.type
class Mutation:
    create_blog: BlogApp = mutations.create(BlogAppInput)
    create_blogs: list[BlogApp] = mutations.create(BlogAppInput)
    update_blogs: list[BlogApp] = mutations.update(BlogAppPartialInput)
    delete_blogs: list[BlogApp] = mutations.delete()

    register: User = auth.register(UserInput)


schema = strawberry.Schema(query=Query, mutation=Mutation)