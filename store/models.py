from django.db import models




class Category(models.Model):
    name_ru = models.CharField(max_length=255)
    name_ro = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return '{}:{}'.format(self.slug, self.name_ru)




class Item(models.Model):
    categories = models.ManyToManyField(Category)
    related_items = models.ManyToManyField('Item', blank=True)
    image = models.ImageField()
    name_ru = models.CharField(max_length=255)
    name_ro = models.CharField(max_length=255)

    def __str__(self):
        return self.name_ru
