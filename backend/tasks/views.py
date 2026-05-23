import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task


# GET + POST /api/
@csrf_exempt
def task_list(request):

    # -------------------
    # GET: return all tasks
    # -------------------
    if request.method == "GET":
        tasks = list(Task.objects.values())
        return JsonResponse(tasks, safe=False)

    # -------------------
    # POST: create task
    # -------------------
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))

            title = data.get("title")
            is_completed = data.get("is_completed", False)

            if not title:
                return JsonResponse(
                    {"error": "title is required"},
                    status=400
                )

            task = Task.objects.create(
                title=title,
                is_completed=is_completed
            )

            return JsonResponse({
                "id": task.id,
                "title": task.title,
                "is_completed": task.is_completed
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse(
                {"error": "Invalid JSON"},
                status=400
            )

        except Exception as e:
            return JsonResponse(
                {"error": str(e)},
                status=500
            )


# OPTIONAL: for unsupported methods
def task_detail(request, pk):
    return JsonResponse({"error": "Not implemented"}, status=405)