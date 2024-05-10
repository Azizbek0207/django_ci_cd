from django.db import models
from django.db.models import Model, CharField, SlugField, ForeignKey, CASCADE, ImageField, IntegerField, DateTimeField, \
    TextField
from django.utils.text import slugify


# Create your models here.

class MainModel(Model):
    title = CharField(max_length=255)
    slug = SlugField(unique=True, editable=False)
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += self.title
        super().save(force_insert, force_update, using, update_fields)


class Category(MainModel):
    pass


class Product(MainModel):
    image = ImageField(upload_to='media')
    price = IntegerField()
    description = TextField()
    status = CharField(max_length=255)
    location = CharField(max_length=255)
    category = ForeignKey('apps.Category', CASCADE)
