from django.urls import path
from todoapp.views import TaskList
from todoapp.views import TaskDetail

urlpatterns = [
    path("", TaskList.as_view()),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
]
