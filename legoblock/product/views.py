from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from .models import Product, ProductType
from .serializers import ProductSerializer, ProductTypeSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

def delete_my_model(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('some-view-name')
    return render(request, 'confirm_delete.html', {'object': obj})      