from django.urls import path

from .views import get_todos, post_todo, update_todo

urlpatterns = [
    path("todo/list", get_todos),
    path("todo", post_todo),
    path("todo/<int:pk>", update_todo)
]

