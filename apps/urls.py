from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import ProductModelViewSet, CategoryListCreateAPIView

router = DefaultRouter()
router.register('product', ProductModelViewSet, 'product')
urlpatterns = [
    path('', include(router.urls)),
    path('category', CategoryListCreateAPIView.as_view(), )
]
