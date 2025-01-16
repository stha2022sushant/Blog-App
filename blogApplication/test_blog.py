import json
from django.test import TestCase, Client
from . factories import BlogFactory
from .models import BlogApp
class TestBlogMutation(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_blog_mutation = '''
        mutation MyMutation {
            createBlog(data: {title: "test", blog: "test"}) {
                id
                blog
                title
                author {
                    pk
                }
            }
        }
        '''
        self.blog_with_author = BlogFactory()

    def test_create_blog_with_author(self):
        response = self.client.post(
            '/graphql',
            json.dumps(
                {
                    'query': self.create_blog_mutation
                }
            ),
            content_type='application/json'
        )
        data = json.loads(response.content)['data']
        self.assertEqual(data['createBlog']['blog'], 'test')
        self.assertEqual(data['createBlog']['title'], 'test')
        

    

