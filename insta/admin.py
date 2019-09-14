from django.contrib import admin
from .models import Post, Comment, User, Like
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'caption', 'created', 'updated', 'like_count')
    list_filter = ['caption']
    search_fields = ['caption']
    fields = ['user','image', 'caption' ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','user', 'content')
    fields = ['post','user', 'content' ]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post','user')
    fields = ['post','user']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass