from rest_framework.response import Response 
from rest_framework.decorators import api_view
from blogApplication.models import BlogApp
from .serializers import BlogAppSerializer


@api_view(['GET'])
def getBlogs(request):
    blogs = BlogApp.objects.all()
    serializer = BlogAppSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addBlogs(request):
    serializer = BlogAppSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
