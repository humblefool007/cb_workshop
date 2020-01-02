from rest_framework import generics
from rest_framework.response import Response

from rest_framework.decorators import api_view

from todos import models
from .serializers import TodoSerializer

@api_view(["GET"])
def get_todos(request):
    todos = models.Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data, status=200)

@api_view(["POST"])
def post_todo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors, status=400)  
    return Response(serializer.data, status=204)


@api_view(["PUT"])
def update_todo(request, pk):
    try:
        todo = models.Todo.objects.get(pk=pk)
    except Exception as e:
        return Response({"error": "record does not exists"}, status=404)
    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors, status=400)
    return Response(serializer.data, status=200)
