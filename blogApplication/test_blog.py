'''from django.test import TestCase


class FakeTest(TestCase):
    """
    This test is for running migrations only
    docker compose run --rm server ./manage.py test -v 2 --pattern="deep/tests/test_fake.py"
    """
    def test_fake(self):
        pass

        '''
from django.test import TestCase, Client
from blogApplication.factory import Factory
from .models import BlogApp

class TestBlogMutation(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = Factory()

    def test_create_blog(self):
        # Step 1: Create a user
        user = UserFactory(username="john_doe", email="john@example.com")

        # Step 2: Define the mutation
        mutation = """
        mutation CreateBlog($title: String!, $blog: String!, $authorId: Int!) {
            createBlog(input: {title: $title, blog: $blog, author: $authorId}) {
                id
                title
                blog
                author {
                    id
                    username
                }
            }
        }
        """

        # Step 3: Execute the mutation
        response = self.factory.graphql_mutation(
            query=mutation,
            variables={
                "title": "My Test Blog",
                "blog": "This is a test blog content.",
                "authorId": user.id,
            },
            client=self.client,
        )

        # Step 4: Assert the response is valid and contains expected fields
        data = response.json()
        
        # Check if the mutation was successful
        self.assertIn("data", data)
        self.assertIn("createBlog", data["data"])

        # Extract the blog response
        blog_data = data["data"]["createBlog"]

        # Check that the blog ID is returned and is an integer
        self.assertIsInstance(blog_data["id"], int)

        # Validate the blog title matches
        self.assertEqual(blog_data["title"], "My Test Blog")

        # Validate the blog content matches
        self.assertEqual(blog_data["blog"], "This is a test blog content.")

        # Validate the author ID matches the user created
        self.assertEqual(blog_data["author"]["id"], user.id)

        # Validate the author's username matches
        self.assertEqual(blog_data["author"]["username"], user.username)

        # Ensure that the blog ID is actually associated with the correct title and content
        blog_instance = BlogApp.objects.get(id=blog_data["id"])
        self.assertEqual(blog_instance.title, blog_data["title"])
        self.assertEqual(blog_instance.blog, blog_data["blog"])

