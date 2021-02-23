from django.shortcuts import render, redirect
from .models import Task
# Create your views here.

def task_list(request):
    tasks = Task.objects.all().order_by('date')

    return render(request,'tasks/task_list.html',{'tasks': tasks})

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('home')

def task_done(request, pk_done):
    task = Task.objects.get(pk=pk_done)
    task.active = False
    task.save(update_fields=["active"])
    return redirect('home')