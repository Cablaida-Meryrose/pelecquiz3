import json
from django.http import JsonResponse
from .models import Task

def task_list(request):

    if request.method == "GET":
        tasks = list(Task.objects.values())
        return JsonResponse(tasks, safe=False)

    if request.method == "POST":
        data = json.loads(request.body)

        task = Task.objects.create(
            title=data.get("title"),
            is_completed=data.get("is_completed", False)
        )

        return JsonResponse({
            "id": task.id,
            "title": task.title,
            "is_completed": task.is_completed
        })