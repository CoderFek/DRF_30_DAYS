from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Product
from django.forms.models import model_to_dict
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer


@api_view(["GET"])
def home_view(request):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(model_data, fields=['id' ,'title', 'price', 'sale_price'])
        # data['sale_price'] = model_data.sale_price
        data = ProductSerializer(instance).data

    return Response(data)