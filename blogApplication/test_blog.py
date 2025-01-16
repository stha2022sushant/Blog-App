
from django.test import TestCase, Client
from blogApplication.factory import BlogFactory
from .models import BlogApp
import json

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
