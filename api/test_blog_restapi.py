from django.test import TestCase
from rest_framework.test import APIClient
from blogApplication.models import BlogApp

class BlogTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()


    def test_create_blog(self):
        payload = {
            "title": "Test Blog",
            "blog": "This is a test blog content."
        }
        response = self.client.post("/add/", payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(BlogApp.objects.count(), 1)
        blog = BlogApp.objects.first()
        self.assertEqual(blog.title, payload["title"])
        self.assertEqual(blog.blog, payload["blog"])

'''

    def test_update_blog(self):
        if not hasattr(self, 'blog'):
            raise AttributeError("Blog object was not created in setUp.")
        payload = {
            "title": "Updated Blog Title",
            "blog": "This is the updated content for the blog post."
        }

        # Make a PUT request to update the blog post
        #url = f"/update/{self.blogs.id}/" 
        url = f"/update/{self.blog.id}/" 
        response = self.client.post(url, payload)

        # Check the status code
        self.assertEqual(response.status_code, 200)

        # Fetch the updated blog from the database
        updated_blog = BlogApp.objects.get(id=self.blog.id)

        # Assert that the blog fields were updated correctly
        self.assertEqual(updated_blog.title, payload["title"])
        self.assertEqual(updated_blog.blog, payload["blog"])

        '''



