from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def api_overview(request):
    return JsonResponse('Api Base Point', safe=False)