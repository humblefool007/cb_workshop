from django.db import models

""" Todo class is a model which holds all the db related attributes """
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

