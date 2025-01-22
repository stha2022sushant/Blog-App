from django.db import models
from django.conf import settings

class BlogApp(models.Model):
    title = models.CharField(max_length=255)
    blog = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    null=True,  # Allow null values in the database
    blank=True,  # Allow this field to be empty in forms
    default=None,  # Set the default to None
)

    class Meta:
        ordering = ['-created_date']
