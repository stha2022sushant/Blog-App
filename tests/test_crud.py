''' from django.test import TestCase
from blogApplication.models import BlogApp
from blogApplication.factories import BlogFactory


class BlogUnitTestCase(TestCase):
    def setUp(self):
        # Create a blog for testing model behavior
        self.blog = BlogApp.objects.create(
            title="Unit Test Blog",
            blog="Unit test content."
        )

    def test_blog_creation(self):
        """Test that a blog is created successfully"""
        blog = BlogApp.objects.get(id=self.blog.id)
        self.assertEqual(blog.title, "Unit Test Blog")
        self.assertEqual(blog.blog, "Unit test content.")

    def test_blog_update(self):
        """Test updating a blog's fields"""
        self.blog.title = "Updated Title"
        self.blog.blog = "Updated content."
        self.blog.save()
        updated_blog = BlogApp.objects.get(id=self.blog.id)
        self.assertEqual(updated_blog.title, "Updated Title")
        self.assertEqual(updated_blog.blog, "Updated content.")

    def test_blog_deletion(self):
        """Test deleting a blog"""
        self.blog.delete()
        self.assertFalse(BlogApp.objects.filter(id=self.blog.id).exists())

'''

from django.test import TestCase
from blogApplication.models import BlogApp
from blogApplication.factories import BlogFactory


class BlogUnitTestCase(TestCase):
    def setUp(self):
        # Create a blog for testing model behavior
        self.blog = BlogApp.objects.create(
            title="Unit Test Blog",
            blog="Unit test content."
        )

    def test_blog_creation(self):
        """Test that a blog is created successfully"""
        blog = BlogApp.objects.get(id=self.blog.id)  # Fetch from the database
        self.assertEqual(blog.title, self.blog.title)  # Compare titles
        self.assertEqual(blog.blog, self.blog.blog)  # Compare blog content

    def test_blog_update(self):
        """Test updating a blog's fields using dynamic data"""
        new_data = BlogFactory.build()  # Generate a new blog instance (not saved to DB)
        self.blog.title = new_data.title  # Update title
        self.blog.blog = new_data.blog  # Update content
        self.blog.save()  # Save the changes

        updated_blog = BlogApp.objects.get(id=self.blog.id)  # Fetch updated blog
        self.assertEqual(updated_blog.title, new_data.title)  # Compare updated titles
        self.assertEqual(updated_blog.blog, new_data.blog)  # Compare updated content

    def test_blog_deletion(self):
        """Test deleting a blog"""
        self.blog.delete()  # Delete the blog
        self.assertFalse(BlogApp.objects.filter(id=self.blog.id).exists())  # Assert it's deleted

