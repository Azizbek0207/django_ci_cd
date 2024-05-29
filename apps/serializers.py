from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.models import Category, Product, Course, CourseCategory, User


# class CategoryModelSerializer(ModelSerializer):
#     product_count = serializers.SerializerMethodField()
#
#     def get_product_count(self, obj):
#         return obj.product_set.count()
#
#     class Meta:
#         model = Category
#         fields = ['id', 'title', 'product_count']
#
#
# class ProductModelSerializer(ModelSerializer):
#     category_title = serializers.CharField(source='category.title', read_only=True)
#
#     class Meta:
#         model = Product
#         fields = ['id', 'title', 'description', 'price', 'status', 'category', 'category_title']

class CourseCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['name']


class CourseModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'price', 'video', 'category']


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'image']
