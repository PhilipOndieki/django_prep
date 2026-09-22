from django.shortcuts import render

# Create your views here
# function based views
from django.http import JsonResponse
from .models import Task

def task_list(request):
    tasks = Task.objects.all().values('id', 'title', 'is_done')
    return JsonResponse(list(tasks), safe=False)
    