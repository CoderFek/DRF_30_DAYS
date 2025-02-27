from django.shortcuts import render
from rest_framework import generics
from api.serializers import ProductSerializer
from api.models import Product

# Create your views here.
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
