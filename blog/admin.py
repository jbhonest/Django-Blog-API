# blog/admin.py

from django.contrib import admin
from .models import Category, Post, Comment


class PostInline(admin.StackedInline):
    model = Post
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    inlines = (PostInline,)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title')
    list_filter = ('category',)
    search_fields = ('title', 'content', 'category__title',
                     'category__description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'text', 'created_at')
    list_filter = ('post',)
    search_fields = ('text',)
