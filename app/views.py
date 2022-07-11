from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from app.forms import TaskCreateForm
from app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "app/index.html"
    queryset = Task.objects.prefetch_related("tags")
    context_object_name = "task_list"


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("app:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("app:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app:index")


def change_task_status(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = not task.completed
    task.save()

    return HttpResponseRedirect(reverse("app:index"))


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tag-list")


class TagListView(generic.ListView):
    model = Tag


