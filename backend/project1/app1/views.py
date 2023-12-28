from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.

class BlogListCreateView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):    
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
