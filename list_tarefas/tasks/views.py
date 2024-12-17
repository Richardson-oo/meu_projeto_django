from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from django.contrib import messages

def tasks_list(request):
    tasks = Tasks.objects.all()
    return render(request, 'tasks_list.html', {'tasks': tasks})

def toggle_task_status(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect( 'tasks_list')

def delete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.delete()
    return redirect('tasks_list')

def delete_all_task(request):
    task = Tasks.objects.all().delete()
    return redirect('tasks_list')


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if not title.strip():
            messages.error(request, "o campo titulo e obrigatorio")
            return render(request, 'add_task.html')
        
        Tasks.objects.create(title=title.strip(), description=description.strip())
        messages.success(request, "Tarefa adicionada com sucesso")
        return redirect('tasks_list')
    return render(request, 'add_task.html')

