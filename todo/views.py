from django.shortcuts import render, redirect

from .models import *
from .forms import *


def home(request):
    tasks = task.objects.all()

    form = TaskForm()
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/home.html', context)


def updateTask(request, pk):
    tasks = task.objects.get(id=pk)

    form = TaskForm(instance=tasks)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('home')

    context ={'form': form}
    return render(request, 'todo/update_task.html', context)


def deleteTask(request, pk):
    item = task.objects.get(id=pk)

    if request.method =='POST':
        item.delete()
        return redirect('home')

    context = {'item': item}
    return render(request, 'todo/delete.html', context)
