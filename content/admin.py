from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['is_active', ]


class PostAdmin(admin.ModelAdmin):
    list_filter = [
        'is_active',
        'is_on_main_page',
        'category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
