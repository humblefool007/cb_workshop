from rest_framework import generics
from rest_framework.response import Response

from rest_framework.decorators import api_view

from todos import models
from .serializers import TodoSerializer

@api_view(["GET"])
def get_todos(request):
    todos = models.Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def post_todo(request):
    print(request.data)
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["PUT"])
def update_todo(request, pk):
    print("sasasasa", pk)
    todo = models.Todo.objects.get(pk=pk)
    print(todo)
    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        err = serializer.is_valid()
        print("sasasasa", err, serializer.errors)
    return Response(serializer.errors, status=400)
