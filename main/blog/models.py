from django.db import models

# Create your models here.


class Post(models.Model):
    heading = models.TextField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
