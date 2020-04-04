from django.shortcuts import render


# Create your views here.


def main_page(request, *args, **kwargs):
    return render(request, "content/base.html")


def category_page(request, *args, **kwargs):
    return render(request, "content/category.html")


def post_page(request, *args, **kwargs):
    return render(request, "content/post.html")


def about_page(request, *args, **kwargs):
    return render(request, "content/about.html")
