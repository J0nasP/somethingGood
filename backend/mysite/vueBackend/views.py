from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser 
from .models import TodoTask
from .serializers import TaskSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

def index(reqeust):
    return HttpResponse("Goodbye world!")

# Create your views here.

@csrf_exempt
def tasks(reqeust):
    if (reqeust.method == 'GET'):
        tasks = TodoTask.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif(reqeust.method == 'POST'):
        data = JSONParser().parse(reqeust)
        serializer = TaskSerializer(data = data)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)

@csrf_exempt
def tasks_details(request, pk):

    try:
        task = TodoTask.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)  

    if(request.method == 'PUT'):
        data = JSONParser().parse(request)  
        serializer = TaskSerializer(task, data=data)
        if(serializer.is_valid()):  
            serializer.save() 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif(request.method == 'DELETE'):
        task.delete() 
        return HttpResponse(status=204) 