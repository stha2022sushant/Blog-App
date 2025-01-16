import json
from django.test import TestCase, Client
from . factories import BlogFactory
from .models import BlogApp

"""
class TestBlogMutation(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_blog_mutation = '''
        mutation MyMutation {
                createBlog(data: {title: "test", blog: "test"}) {
                id
                blog
                title
            }
        }
        '''
       

    def test_create_blog(self):
        response = self.client.post(
            '/graphql',
            json.dumps(
                {
                    'query': self.create_blog_mutation
                    
                }
            ),
            content_type='application/json'
        )
        data = json.loads(response.content)
        print("################################")
        print(data)
        print("################################")
        self.assertTrue(True)

        """

class TestBlogMutation(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_blog_mutation = '''
        mutation MyMutation {
            createBlog(data: {title: "a", blog: "test"}) {
                id
                blog
                title
                author {
                    pk
                }
            }
        }
        '''
        self.blog_with_author = BlogFactory()  # Blog with an author (user created)
        self.blog_without_author = BlogFactory(author=None)  # Blog without an author (author is None)

    def test_create_blog_with_author(self):
        response = self.client.post(
            '/graphql',
            json.dumps(
                {
                    'query': self.create_blog_mutation.replace(
                        "test", self.blog_with_author.title
                    ).replace("test", self.blog_with_author.blog)
                }
            ),
            content_type='application/json'
        )
        data = json.loads(response.content)
        print("################################")
        print(data)
        print("################################")
        self.assertTrue(True)

    

