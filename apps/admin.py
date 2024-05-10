from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass

@admin.register(Category)
class ProductAdmin(ModelAdmin):
    pass

