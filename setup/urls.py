from django.contrib import admin
from django.urls import path
from tasks.views import task_list, home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home_view"),
    path("lista/", task_list, name="task_list"),
]