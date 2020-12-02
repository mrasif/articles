from django.urls import path
from .views import BlogListAPIView

app_name = 'blog'

urlpatterns = [
    path('', BlogListAPIView.as_view(), name='blogs')
]