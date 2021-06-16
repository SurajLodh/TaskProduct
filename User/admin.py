from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post


# @admin.register(User)
# class UserModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'first_name', 'last_name', 'email', 'password', 'username']

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'text', 'created_at', 'updated_at']