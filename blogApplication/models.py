from django.db import models
'''
class BlogApp(models.Model):
    title = models.CharField(max_length=255)  # Blog title
    blog = models.TextField()  # Blog content
    created_date = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updated_date = models.DateTimeField(auto_now=True) 


    class Meta:
        ordering = ['-created_date']

        

'''


from django.conf import settings

class BlogApp(models.Model):
    title = models.CharField(max_length=255)
    blog = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['-created_date']
