# blog/admin.py

from django.contrib import admin
from .models import Category, Post, Comment


class PostInline(admin.StackedInline):
    model = Post
    extra = 1


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_active',
                    'created_date', 'updated_date')
    list_display_links = ('id', 'title')
    list_filter = ('is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    search_fields = ('title', 'description')
    inlines = (PostInline,)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'is_active',
                    'created_date', 'updated_date')
    list_display_links = ('id', 'title')
    list_filter = ('category', 'is_active', 'created_date', 'updated_date')
    list_editable = ('is_active',)
    search_fields = ('title', 'content', 'category__title',
                     'category__description')
    inlines = (CommentInline,)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'post', 'is_active',
                    'created_date', 'updated_date')
    list_filter = ('post', 'is_active', 'author',
                   'created_date', 'updated_date')
    list_editable = ('is_active',)
    search_fields = ('text',)
