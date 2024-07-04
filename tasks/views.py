from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from .models import Task


class TaskListView(ListView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    fields = ["title", "deadline"]
    success_url = reverse_lazy('task_list')


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["title", "deadline"]
    success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
    model = Task
    lookup_field = "id"
    success_url = reverse_lazy('task_list')


class TaskCompleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.mark_has_complete()
        return redirect('task_list')
