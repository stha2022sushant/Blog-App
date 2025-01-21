""" import json
from django.test import TestCase, Client
from .factories import BlogFactory  # Import the BlogFactory to generate blog data

class TestBlogMutation(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Generate a blog using BlogFactory (author may or may not be present)
        # self.blog = BlogFactory()  # This will create a blog with random title, content, and optional author

        # GraphQL mutation to create a blog
        self.create_blog_mutation = '''
        mutation MyMutation ($title: String!, $blog: String!) {
          createBlog(data: {title: $title, blog: $blog}) {
            id
          }
        }
        '''

        self.update_blog_mutation = '''
        mutation MyMutation ($title: String!, $blog: String!) {
          updateBlog(blogData: {title: $title, blog: $blog}) {
            id
            
          }
        }
        '''

        self.delete_blog_mutation = '''
        mutation MyMutation ($blogId: ID!) {
          deleteBlog(blogId: $blogId)
        }
        '''

        self.blogs = BlogFactory.create()
        data = self.blogs
        print("################################")
        print(data)
        print("################################")



    def test_create_blog(self):
        # Prepare variables to pass into the GraphQL mutation
        variables = {
            'title': self.blog.title,  # Generated title from factory
            'blog': self.blog.blog     # Generated blog content from factory
        }
    
        # Send the mutation request
        response = self.client.post(
            '/graphql',
            json.dumps({'query': self.create_blog_mutation, 'variables': variables}),
            content_type='application/json'
        )
        
        # Load the response and check the data
        response_data = json.loads(response.content)
        print(response_data)  # Print the full response for debugging
    
        data = response_data.get('data')
        
        # Check if 'createBlog' exists in the response
        if data and data.get('createBlog'):
            created_blog_id = data['createBlog']['id']
            self.assertEqual(str(created_blog_id), str(self.blog.id))  # Compare the dynamic ID
        else:
            # Check for errors in the response if 'createBlog' is not present
            errors = response_data.get('errors')
            if errors:
                print(errors)  # Print the errors for debugging
            self.fail("Blog creation failed, 'createBlog' is not in the response.")

    """


