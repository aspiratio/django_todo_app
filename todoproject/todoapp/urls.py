from django.urls import path
from todoapp.views import TaskList

urlpatterns = [path("", TaskList.as_view())]
