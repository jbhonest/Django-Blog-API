# blog/models.py
from django.db import models


class MyBaseModel(models.Model):
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(MyBaseModel):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Post(MyBaseModel):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return self.title


class Comment(MyBaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f'{self.author} - {self.text}'
