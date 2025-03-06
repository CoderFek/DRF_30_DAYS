from django.shortcuts import render
from rest_framework import generics
from api.serializers import ProductSerializer
from api.models import Product

from api.mixins import StaffEditorPermissionMixin

from rest_framework.response import Response


# Create your views here.

class ProductListCreateView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(content=content)
        return Response(serializer.data)

product_create_view = ProductListCreateView.as_view()
        

class ProductDetailView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailView.as_view()


class ProductUpdateView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.content is None:
            instance.content = instance.title

product_update_view = ProductUpdateView.as_view()


class ProductDeleteView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        #instance operations if any
        super().perform_destroy(instance)

product_delete_view = ProductDeleteView.as_view()