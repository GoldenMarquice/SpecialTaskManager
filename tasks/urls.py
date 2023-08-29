from django.urls import path
from tasks import views

urlpatterns = [
    path("tasks-list/", views.TasksListView.as_view(), name="tasks-list"),
    path("completed/", views.CompletedListView.as_view(), name="completed"),
    path("inprogress/", views.InProgressListView.as_view(), name="inprogress"),
    path("todo/", views.ToDoListView.as_view(), name="todo"),
    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/update_task/", views.UpdateTaskView.as_view(), name="update"),  
    path("<int:pk>/delete_task/", views.DeleteTaskView.as_view(), name="delete"), 
    path("create/", views.CreateTaskView.as_view(), name="create"),
]





