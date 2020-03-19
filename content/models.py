from django.db import models
from .managers import PostManager, CategoryManager


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(db_index=True)

    objects = CategoryManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('title',)


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(db_index=True)
    is_on_main_page = models.BooleanField(
        default=True, db_index=True)
    objects = PostManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('title',)
