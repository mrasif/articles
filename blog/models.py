from django.db import models
from django.contrib.auth import get_user_model


class Blog(models.Model):
    author = models.ForeignKey(to=get_user_model(), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
