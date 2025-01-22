from rest_framework import serializers
from blogApplication.models import BlogApp

class BlogAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogApp
        fields = '__all__'
        # Alternatively, we can specify specific fields:
        # fields = ['id', 'title', 'content', 'created_at']


