from rest_framework.response import Response 
from rest_framework.decorators import api_view
from blogApplication.models import BlogApp
from .serializers import BlogAppSerializer


@api_view(['GET'])
def getData(request):
    blogs = BlogApp.objects.all()
    serializer = BlogAppSerializer(blogs, many=True)
    return Response(serializer.data)