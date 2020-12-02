from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from blog.models import Blog
from blog.serializers import BlogSerializer


class BlogListAPIView(GenericAPIView):

    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.all()

    def get(self, request, *args, **kwargs):
        """
        List of Blog
        :return: list of serialized blog
        """
        blogs = self.get_queryset()
        serializer = self.get_serializer(blogs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create Blog
        :return: newly created blog object
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)