from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from blog.models import Blog


class BlogListAPIView(GenericAPIView):

    def get_queryset(self):
        return Blog.objects.all()

    def get(self, request, *args, **kwargs):
        blogs = self.get_queryset()
        print(blogs)
        return Response(data={}, status=status.HTTP_200_OK)