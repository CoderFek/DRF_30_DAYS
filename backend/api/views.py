from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Product
from django.forms.models import model_to_dict
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def home_view(request):
    model_data = Product.objects.all().order_by("?").first()

    if model_data:
        data = model_to_dict(model_data, fields=['id' ,'title', 'price', 'sale_price'])
        data['sale_price'] = model_data.sale_price

    return Response(data, headers={"content-type":"application/json"})