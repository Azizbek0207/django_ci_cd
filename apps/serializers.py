from rest_framework.serializers import ModelSerializer

from apps.models import Category, Product


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug']
