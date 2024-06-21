from django.contrib import admin
from django.urls import path
from tasks.views import TaskListView, TaskCreateView, TaskUpdateView, home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home_view"),
    path("lista/", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_form"),
    path("update/<int:pk>", TaskUpdateView.as_view(), name="task_update")
]