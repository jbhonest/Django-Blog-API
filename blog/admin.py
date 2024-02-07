# blog/admin.py

from django.contrib import admin
from .models import Category, Post, Comment


class PostInline(admin.StackedInline):
    model = Post
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_active',
                    'created_date', 'updated_date')
    list_display_links = ('id', 'title')
    list_filter = ('is_active', 'created_date', 'updated_date')
    search_fields = ('title', 'description')
    inlines = (PostInline,)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'is_active',
                    'created_date', 'updated_date')
    list_display_links = ('id', 'title')
    list_filter = ('category', 'is_active', 'created_date', 'updated_date')
    search_fields = ('title', 'content', 'category__title',
                     'category__description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'text', 'is_active',
                    'created_date', 'updated_date')
    list_filter = ('post', 'is_active',
                   'created_date', 'updated_date')
    search_fields = ('text',)
