import strawberry
import strawberry_django
from strawberry_django import auth, mutations
from asgiref.sync import sync_to_async
from . models import BlogApp as BlogAppModel

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

    #update_blogs: list[BlogApp] = mutations.update(BlogAppPartialInput)

    @strawberry.mutation
    @sync_to_async
    def update_blog(self, info, blog_data: BlogAppPartialInput) -> BlogApp:
        blog_instance = BlogAppModel.objects.get(id=blog_data.id)
        
        if blog_data.title:
            blog_instance.title = blog_data.title
        if blog_data.blog:
            blog_instance.blog = blog_data.blog
        #if blog_data.author:
        #    blog_instance.author = blog_data.author
        
        blog_instance.save()
        return blog_instance
    #delete_blogs: list[BlogApp] = mutations.delete()

    @strawberry.mutation
    @sync_to_async
    def delete_blog(self, info, blog_id: int) -> str:
        try:
            blog_instance = BlogAppModel.objects.get(id=blog_id)
            blog_instance.delete()
            return f"Blog with ID {blog_id} has been deleted successfully."
        except BlogAppModel.DoesNotExist:
            return f"Blog with ID {blog_id} does not exist."


    

    register: User = auth.register(UserInput)

schema = strawberry.Schema(query=Query, mutation=Mutation)
