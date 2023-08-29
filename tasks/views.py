from typing import Any, Dict
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from django.views.generic import ListView

from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin
)

class TasksListView(ListView):
    template_name = "tasks/tasks_list.html"
    model = Task

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     status = Status.objects.get(name="alltasks")
    #     context["tasks"] = Task.objects.filter(
    #         status=status
    #     ).order_by("created_on").reverse()
    #     return context
    
class ToDoListView(LoginRequiredMixin, ListView):
    template_name = "tasks/todo_list.html"
    model = Task
    context_object_name = "todo"

    def get_queryset(self):
        return Task.objects.filter(status=0)
    
class InProgressListView(LoginRequiredMixin, ListView):
    template_name = "tasks/inprogress_list.html"
    model = Task
    context_object_name = "inprogress"

    def get_queryset(self):
        return Task.objects.filter(status=1)

class CompletedListView(LoginRequiredMixin, ListView):
    template_name = "tasks/completed_list.html"
    model = Task
    context_object_name = "completed"

    def get_queryset(self):
        return Task.objects.filter(status=2)
    
class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = "tasks/create_task.html"
    model = Task
    fields = "__all__"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class UpdateTaskView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "tasks/update_task.html"
    model = Task
    fields = "__all__"

    def test_func(self):
        Task = self.get_object()
        return self.request.user == Task.author
    
class DeleteTaskView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "tasks/delete_task.html"
    model = Task
    success_url = reverse_lazy("list")

    def test_func(self):
        Task = self.get_object()
        return self.request.user == Task.author