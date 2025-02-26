from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Product
from django.forms.models import model_to_dict
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer


@api_view(["POST"])
def home_view(request):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        # serializer.save()
        print(serializer.data)
        return Response(serializer.data)