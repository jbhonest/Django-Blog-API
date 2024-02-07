# blog/views.py
from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Category, Comment
from .serializers import PostSerializer, CategorySerializer, CommentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.filter(is_active=True).order_by('-pk')
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    search_fields = ('title', 'description')


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.filter(is_active=True).order_by('-pk')
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('category',)
    search_fields = ('title', 'content')


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(is_active=True).order_by('-pk')
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('post', 'author')
    search_fields = ('text', 'author')
