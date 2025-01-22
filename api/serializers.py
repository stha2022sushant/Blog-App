from rest_framework import serializers
from blogApplication.models import BlogApp

class BlogAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogApp
        fields = '__all__'


