from django.urls import path

from apps.views import CategoryDeleteApiView, ProductListApiView

urlpatterns = [
    path('category/<pk>', CategoryDeleteApiView.as_view()),
    path('product', ProductListApiView.as_view())
]
