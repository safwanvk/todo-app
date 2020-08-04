from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'list': '/task-list/',
        'detail-view': '/task-detail/<str:pk>/',
        'create': '/task-create/',
        'update': '/task-update/<str:pk>/',
        'delete': '/task-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def task_detail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    
    return Response(serializer.data)