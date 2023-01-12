from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import TodoSerializer
from .models import TodoItem

@csrf_exempt
def todo_items(request):
    #Get the  list of items
    if(request.method == 'GET'):
        todoItems = TodoItem.objects.all()
        serializer = TodoSerializer(todoItems, many=True)
        return JsonResponse(serializer.data, safe=False)
    #Post to the db
    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = TodoSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)

@csrf_exempt
def todo_items_details(request, pk):
    try:
        todo_item= TodoItem.objects.get(pk=pk)

    except:
        return HttpResponse(status=404)

    if (request.method == 'PUTT'):
        data = JSONParser().parse(request)
        serializer = TodoSerializer(todo_item, data=data)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)
    
    elif(request.method == 'DELETE'):
        todo_item.delete()
        return HttpResponse(status=204)