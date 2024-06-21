from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Task


def home_view(request):
    return render(request, "tasks/home_view.html")


class TaskListView(ListView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    fields = ["title", "deadline"]
    success_url = reverse_lazy('task_list')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "New task created successfully")
        return response

class TaskUpdateView(UpdateView):
    model = Task
    fields = ["title", "deadline"]
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Task updated successfully")
        return response
