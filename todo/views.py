from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def TaskListView(request):
    tasks = Task.objects.all().filter(author=request.user)
    search_query = request.GET.get("search", "")
    if search_query:
        tasks = tasks.filter(title__icontains=search_query)
    return render(
        request,
        "tasks_list.html",
        context={
            "tasks": tasks,
            "search_query": search_query,
        },
    )


@login_required
def TaskCreateView(request):
    form = TaskForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect("task-list")
    else:
        form = TaskForm()
    return render(request, "task_create.html", context={"form": form})


@login_required
def TaskUpdateView(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if task.author != request.user:
        return render(request, "access_denied.html")
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task-list")
    else:
        form = TaskForm(instance=task)
    return render(request, "task_update.html", context={"form": form})


@login_required
def TaskDeleteView(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if task.author != request.user:
        return render(request, "access_denied.html")
    if request.method == "POST":
        task.delete()
        return redirect("task-list")
    return render(request, "task_delete.html", context={"task": task})
