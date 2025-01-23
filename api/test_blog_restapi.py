from django.test import TestCase
from rest_framework.test import APIClient
from blogApplication.models import BlogApp


class BlogTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a blog post for update and delete tests
        self.blog = BlogApp.objects.create(
            title="Initial Blog Title",
            blog="Initial blog content."
        )

    def test_create_blog(self):
        """Test for creating a blog post"""
        payload = {
            "title": "Test Blog",
            "blog": "This is a test blog content."
        }
        response = self.client.post("/add/", payload, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(BlogApp.objects.count(), 2)  # Includes the blog created in setUp
        blog = BlogApp.objects.latest("id")
        self.assertEqual(blog.title, payload["title"])
        self.assertEqual(blog.blog, payload["blog"])

    def test_update_blog(self):
            """Test for updating an existing blog post"""
            payload = {
                "title": "Updated Blog Title",
                "blog": "This is the updated content for the blog post."
            }
            response = self.client.post(f"/update/{self.blog.id}/", payload, format="json")
            self.assertEqual(response.status_code, 200)

            # Fetch the updated blog from the database
            updated_blog = BlogApp.objects.get(id=self.blog.id)
            self.assertEqual(updated_blog.title, payload["title"])
            self.assertEqual(updated_blog.blog, payload["blog"])

    def test_delete_blog(self):
        """Test for deleting an existing blog post"""
        response = self.client.delete(f"/delete/{self.blog.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(BlogApp.objects.count(), 0)
        self.assertFalse(BlogApp.objects.filter(id=self.blog.id).exists())


        



