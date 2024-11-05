from django.shortcuts import render
from django.http import JsonResponse
import json


# Create your views here.
def api_home(request):
    body = request.body  # byte string of json data
    print(request.GET)
    print(request.POST)
    data = {}
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return JsonResponse({"success": False, "message": "Invalid JSON data"})
    # data["headers"] = request.headers
    data["content_type"] = request.content_type
    return JsonResponse(
        {"success": True, "message": "Welcome to the API", "data": data}
    )
