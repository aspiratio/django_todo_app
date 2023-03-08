from django.urls import path
from todoapp.views import TaskList
from todoapp.views import TaskDetail
from todoapp.views import TaskCreate
from todoapp.views import TaskUpdate
from todoapp.views import TaskDelete
from todoapp.views import TaskListLoginView

urlpatterns = [
    path("", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("create-task/", TaskCreate.as_view(), name="create-task"),
    path("edit-task/<int:pk>/", TaskUpdate.as_view(), name="edit-task"),
    path("delete-task/<int:pk>/", TaskDelete.as_view(), name="delete-task"),
    path("login/", TaskListLoginView.as_view(), name="login"),
]
