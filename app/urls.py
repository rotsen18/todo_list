from django.urls import path, include

from app.views import (
    TaskCreateView,
    TaskUpdateView,
    TaskListView,
    TaskDeleteView,
    TaskDetailView,
    change_task_status,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TagListView,

)

urlpatterns = [
    path(
        "",
        TaskListView.as_view(),
        name="task-list"
    ),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/",
        TaskDetailView.as_view(),
        name="task-detail"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasks/<int:pk>/change/",
        change_task_status,
        name="task-change"
    ),

    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
]

app_name = "app"
