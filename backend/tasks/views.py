from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def task_list(request):

    if request.method == 'GET':
        return Response(Task.objects.values())

    if request.method == 'POST':
        title = request.data.get("title")

        if not title:
            return Response({"error": "title required"}, status=400)

        task = Task.objects.create(title=title)
        return Response({"message": "created"})