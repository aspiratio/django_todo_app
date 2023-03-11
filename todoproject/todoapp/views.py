from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from todoapp.models import Task


# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)

        searchInputText = self.request.GET.get("search") or ""
        if searchInputText:
            context["tasks"] = context["tasks"].filter(
                title__startswith=searchInputText
            )

        context["search"] = searchInputText

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("tasks")


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = "__all__"  # ["user", "title", ....] と書くのと同じ意味（全部のフィールドを指定したいときに便利）
    success_url = reverse_lazy("tasks")
    # デフォルトの context_object_name は object (object_list)、またはモデルに設定したクラスを小文字に変えたもの task (task_list)である
    # https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-display/
    # あえて"task"と設定する必要はないが明示的に指定した方がわかりやすいので設定しておく
    context_object_name = "task"


class TaskListLoginView(LoginView):
    fields = "__all__"  # Userモデルのfieldを全部使うという意味
    template_name = "todoapp/login.html"

    def get_success_url(self):
        return reverse_lazy("tasks")


class RegisterTodoApp(FormView):
    template_name = "todoapp/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
