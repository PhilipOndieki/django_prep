from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import JsonResponse
from .models import Task
import json

class TaskListCreateView(View):

    def get(self, request):
        tasks = list(Task.objects.all().values())
        return JsonResponse(tasks, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        task = Task.objects.create(title=data['title'], description=data.get('description', ''))
        return JsonResponse({'id': task.id, 'title': task.title}, status=201)


class TaskDetailView(View):

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return None

    def get(self, request, pk):
        task = self.get_object(pk)
        if not task:
            return JsonResponse({'error': 'Task not found'}, status=404)
        return JsonResponse({'id': task.id, 'title': task.title, 'description': task.description, 'is_done': task.is_done})

    def put(self, request, pk):
        task = self.get_object(pk)
        if not task:
            return JsonResponse({'error': 'Task not found'}, status=404)
        data = json.loads(request.body)
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.is_done = data.get('is_done', task.is_done)
        task.save()
        return JsonResponse({'id': task.id, 'title': task.title, 'description': task.description, 'is_done': task.is_done})

    def delete(self, request, pk):
        task = self.get_object(pk)
        if not task:
            return JsonResponse({'error': 'Task not found'}, status=404)
        task.delete()
        return JsonResponse({}, status=204)