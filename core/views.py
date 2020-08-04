from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'list': '/task/list/',
        'detail-view': '/task-detail/<str:pk>/',
        'create': '/task-create',
        'update': '/task-update/<str:pk>/',
        'delete': '/task-delete/<str:pk>/'
    }
    return Response(api_urls)