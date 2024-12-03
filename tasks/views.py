from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TaskForm
from tasks.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "tasks/task_list.html"
    ordering = ["status", "-created_at"]
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TaskForm()
        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        return queryset

class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:task-list")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "tasks/tag_list.html"
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    template_name = "tasks/tag_form.html"
    success_url = reverse_lazy("tasks:tag-list")

class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    template_name = "tasks/tag_form.html"
    success_url = reverse_lazy("tasks:tag-list")

class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "tasks/tag_confirm_delete.html"
    success_url = reverse_lazy("tasks:tag-list")


def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = not task.status
    task.save()
    return redirect("tasks:task-list")
