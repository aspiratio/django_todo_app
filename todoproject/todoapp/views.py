from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from todoapp.models import Task


# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = "tasks"


class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"


class TaskCreate(CreateView):
    model = Task
    fields = "__all__"  # ["user", "title", ....] と書くのと同じ意味（全部のフィールドを指定したいときに便利）
    success_url = reverse_lazy("tasks")


class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"  # ["user", "title", ....] と書くのと同じ意味（全部のフィールドを指定したいときに便利）
    success_url = reverse_lazy("tasks")
