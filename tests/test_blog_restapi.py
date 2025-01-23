from django.test import TestCase
from rest_framework.test import APIClient
from blogApplication.models import BlogApp
from blogApplication.factories import BlogFactory


class BlogIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a blog for testing update and delete API endpoints
        self.blog = BlogApp.objects.create(
            title="Initial Blog Title",
            blog="Initial blog content."
        )

    def test_create_blog(self):
        
        """Integration test for creating a blog post"""
        payload = {
            "title": "Integration Test Blog",
            "blog": "This is an integration test blog content."
        }
        
        #payload = BlogFactory()
        response = self.client.post("/add/", payload, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(BlogApp.objects.count(), 2)
        created_blog = BlogApp.objects.latest("id")
        self.assertEqual(created_blog.title, payload["title"])
        self.assertEqual(created_blog.blog, payload["blog"])

    def test_update_blog(self):
        """Integration test for updating a blog post using BlogFactory"""
        # Generate new dynamic data for update
        new_data = BlogFactory.build()  # Builds a BlogFactory instance without saving it
        payload = {
            "title": new_data.title,
            "blog": new_data.blog,
        }
        response = self.client.post(f"/update/{self.blog.id}/", payload, format="json")
        self.assertEqual(response.status_code, 200)

        # Verify the blog is updated in the database
        updated_blog = BlogApp.objects.get(id=self.blog.id)
        self.assertEqual(updated_blog.title, new_data.title)
        self.assertEqual(updated_blog.blog, new_data.blog)

    def test_delete_blog(self):
        """Integration test for deleting a blog post"""
        response = self.client.delete(f"/delete/{self.blog.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(BlogApp.objects.count(), 0)
        self.assertFalse(BlogApp.objects.filter(id=self.blog.id).exists())
