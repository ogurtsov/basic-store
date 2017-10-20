from django.db import models
from django.utils.translation import get_language




class Category(models.Model):
    name_ru = models.CharField(max_length=255)
    name_ro = models.CharField(max_length=255)
    is_visible = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    @property
    def name(self):
        if get_language() == 'ru':
            return self.name_ru
        return self.name_ro

    def __str__(self):
        return '{}:{}'.format(self.slug, self.name_ru)




class Item(models.Model):
    categories = models.ManyToManyField(Category)
    related_items = models.ManyToManyField('Item', blank=True)
    image = models.ImageField()
    name_ru = models.CharField(max_length=255)
    name_ro = models.CharField(max_length=255)
    amount_left = models.IntegerField(default=0)

    @property
    def name(self):
        if get_language() == 'ru':
            return self.name_ru
        return self.name_ro

    def __str__(self):
        return '{}:{}'.format(self.pk, self.name_ru)
