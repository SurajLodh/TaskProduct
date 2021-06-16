from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    