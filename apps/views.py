from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, DestroyAPIView

from apps.models import Category, Product
from apps.serializers import CategoryModelSerializer, ProductModelSerializer


# Create your views here.
# class CategoryListApiView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryModelSerializer


class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class CategoryDeleteApiView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
