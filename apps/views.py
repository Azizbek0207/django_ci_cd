from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.openapi import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.filters import CourseFilter
from apps.models import Course, User
from apps.serializers import CourseModelSerializer, UserProfileSerializer


# from apps.serializers import CategoryModelSerializer, ProductModelSerializer


# Create your views here.
# class CategoryListApiView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class =s CategoryModelSerializer


# class ProductListAPIView(ListAPIView):
#     queryset = Product.objects.select_related('category')
#     serializer_class = ProductModelSerializer
#     # filterset_class = ProductFilter
#     # filterset_fields = {
#     #     'price': ['gte', 'lte'],
#     #     "status": ["icontains"],
#     # }
#
#
# class CategoryListCreateAPIView(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryModelSerializer


class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CourseFilter


class CourseCreateAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)


class UserProfileAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer
