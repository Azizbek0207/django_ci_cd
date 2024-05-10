from django.shortcuts import render
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from apps.filters import ProductFilter
from apps.models import Category, Product
from apps.serializers import CategoryModelSerializer, ProductModelSerializer


# Create your views here.
# class CategoryListApiView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.select_related('category')
    serializer_class = ProductModelSerializer
    # filter_backends = [DjangoFilterBackend]
    # ordering_fields = ['created_at']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "price": ['lte'],

        "slug": ["contains"],
        "description": ["contains"],
    }
    filter_class = ProductFilter


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
