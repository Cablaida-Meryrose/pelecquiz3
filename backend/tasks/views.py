import json
from django.http import JsonResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def task_list(request):

    if request.method == "GET":
        tasks = list(Task.objects.values())
        return JsonResponse(tasks, safe=False)

    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))

            if "title" not in data:
                return JsonResponse({"error": "title is required"}, status=400)

            task = Task.objects.create(
                title=data["title"],
                is_completed=data.get("is_completed", False)
            )

            return JsonResponse({
                "id": task.id,
                "title": task.title,
                "is_completed": task.is_completed
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)