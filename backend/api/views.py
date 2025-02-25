from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Product
from django.forms.models import model_to_dict
import json

# Create your views here.
def home_view(request):
    model_data = Product.objects.all().order_by("?").first()

    if model_data:
        data = model_to_dict(model_data, fields=['id' ,'title', 'price'])

    return HttpResponse(data, headers={"content-type":"application/json"})