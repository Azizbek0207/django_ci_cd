from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.views import CourseListAPIView, CourseCreateAPIView, UserProfileAPIView

# from apps.views import ProductListAPIView, CategoryListCreateAPIView

urlpatterns = [
    # path('product/', ProductListAPIView.as_view(), name='product'),
    # path('category', CategoryListCreateAPIView.as_view(), ),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('course-list', CourseListAPIView.as_view(), name='course-list'),
    path('course-create', CourseCreateAPIView.as_view(), name='course-create'),
    path('profile/<int:pk>', UserProfileAPIView.as_view(), name='profile'),
]
