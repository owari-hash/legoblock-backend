from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet , OrderItemViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'order-item', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]