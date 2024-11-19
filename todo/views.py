from django.shortcuts import render, get_object_or_404
from .models import Task
from django.http import JsonResponse

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        task_title = request.POST.get('title', '').strip()
        if not task_title:
            return JsonResponse({'error': 'Title cannot be empty!'}, status=400)
        if Task.objects.filter(title=task_title).exists():
            return JsonResponse({'error': 'Task already exists!'}, status=400)
        task = Task.objects.create(title=task_title)
        return JsonResponse({'message': 'Task added successfully!', 'task_id': task.id}, status=201)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)

def delete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully!'}, status=200)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)
