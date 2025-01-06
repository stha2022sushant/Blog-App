from django.db import models

class BlogApp(models.Model):
    title = models.CharField(max_length=255)  # Blog title
    blog = models.TextField()  # Blog content
    created_date = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updated_date = models.DateTimeField(auto_now=True) 

'''
    class Meta:
        ordering = ['-created_date']

        '''