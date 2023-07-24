from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def json_view(request):
    data={
        "Name":"Kanhaya",
        "Age":25,
        "Address":"BBSR"
    }
    return JsonResponse(data)
    