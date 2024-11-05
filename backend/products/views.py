from django.shortcuts import render
from django.http import JsonResponse
from .models import Product


# Create your views here.
def home(request):
    model_data = Product.objects.all().order_by("?").first()
    data = {
        "id": model_data.id,
        "title": model_data.title,
        "content": model_data.content,
        "price": model_data.price,
    }
    return JsonResponse({"data": data})
