from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from .models import Product, ProductType
from .serializers import ProductSerializer, ProductTypeSerializer

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from product.models import Product
from product.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'price_mnt': ['gte', 'lte'],
        'delivery_type': ['exact'],
        'in_stock': ['exact'],
    }
    search_fields = ['name', 'description', 'tags']
    ordering_fields = ['created_at', 'price_mnt', 'name']

    # Optionally, override get_queryset to add custom filtering logic


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

def delete_my_model(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('some-view-name')
    return render(request, 'confirm_delete.html', {'object': obj})      