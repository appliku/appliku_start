from django.urls import path
from .views import *

urlpatterns = [
    path('category', category_page),
    path('post', post_page),
    path('about', about_page),
    path('', main_page),

]
