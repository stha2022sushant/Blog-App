import json
import pytest
from django.test import TestCase, Client
from . factories import BlogFactory

class TestBlogMutation(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_blog_mutation = '''
        mutation CreateBlog($title: String!, $blog: String!) {
          createBlog(data: {title: $title, blog: $blog}) {
            id
            title
            blog
          }
        }
        '''
        self.update_blog_mutation = '''
        mutation UpdateBlog($id: ID!, $title: String!, $blog: String!) {
          updateBlog(blogData: {id: $id, title: $title, blog: $blog}) {
            id
            title
            blog
          }
        }
        '''

        self.delete_blog_mutation = '''
        mutation DeleteBlog($id: ID!) {
          deleteBlog(id: $id) {
            success
            message
          }
        }
        '''

    def test_create_blog(self):
        
        variables = {
            'title': "Test Blog Title",
            'blog': "This is the content of the test blog."
        }

        response = self.client.post(
            '/graphql',
            json.dumps({'query': self.create_blog_mutation, 'variables': variables}),
            content_type='application/json'
        )

        response_data = json.loads(response.content)

        print("#############################")
        print(response_data)
        print("#############################")

        self.assertNotIn('errors', response_data, f"Errors occurred: {response_data.get('errors')}")
        self.assertIn('data', response_data)
        self.assertIn('createBlog', response_data['data'])

        created_blog_id = response_data['data']['createBlog']['id']
        self.assertIsNotNone(created_blog_id)
        print(f"Created Blog ID: {created_blog_id}")

   # def test_update_existing_blog(self):
        #created_blog = BlogFactory()
        updated_blog_data = BlogFactory.build()
        #created_blog = BlogFactory()  # Create a blog using BlogFactory
        variables = {
            'id': created_blog_id,  # Use the created blog ID
            'title': updated_blog_data.title,  # Updated title
            'blog': updated_blog_data.blog  # Updated content
        }

        update_response = self.client.post(
            '/graphql',
            json.dumps({'query': self.update_blog_mutation, 'variables': variables}),
            content_type='application/json'
        )

        updated_response_data = json.loads(update_response.content)

        print("#############################")
        print(updated_response_data)
        print("#############################")

        self.assertNotIn('errors', updated_response_data, f"Errors occurred: {updated_response_data.get('errors')}")
        self.assertIn('data', updated_response_data)
        self.assertIn('updateBlog', updated_response_data['data'])

        updated_blog = updated_response_data['data']['updateBlog']
        self.assertEqual(updated_blog['id'], str(variables['id']))
        self.assertEqual(updated_blog['title'], variables['title'])
        self.assertEqual(updated_blog['blog'], variables['blog'])

        print(f"Updated Blog: {updated_blog}")

    

        
