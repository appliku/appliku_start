from django.db import models
from django.apps import apps


class PostQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def main_page(self):
        return self.filter(is_on_main_page=True)


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def main_page(self):
        return self.get_queryset().active().main_page()


class CategoryQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)


class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()
