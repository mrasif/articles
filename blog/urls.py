from django.urls import path
from .views import BlogListAPIView, BlogRetrieveUpdateDestroyAPIView

app_name = 'blog'

urlpatterns = [
    path('', BlogListAPIView.as_view(), name='blogs'),
    path('<int:id>/', BlogRetrieveUpdateDestroyAPIView.as_view(), name='blog'),
]