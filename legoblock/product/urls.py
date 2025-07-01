from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductTypeViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'product-types', ProductTypeViewSet)  


urlpatterns = [
    path('', include(router.urls)),
    
]