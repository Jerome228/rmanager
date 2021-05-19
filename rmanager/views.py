from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.shortcuts import render, redirect
from api.models import AppData
from .forms import TaskSubmitForm
from django.urls import reverse
from django.contrib import messages
from celery.result import AsyncResult
from .tasks import c_runCommands


def remoteTask(request):
    try:
        if 'task_data' in request.session:
            task_data = request.session['task_data']
            del request.session['task_data']
        else:
            messages.add_message(request, messages.INFO, "No job data found. Klindly lunch a new job.") 
            return redirect(reverse('home'))           
        queryset = AppData.objects.filter(trg=task_data['trg']).last()
        if not queryset:
            raise Exception(f'No {task_data["trg"]} App found.')
        srv = queryset.hservers        
        task = c_runCommands.delay(srv)
        messages.add_message(request, messages.INFO, "Job submitted. The output from the tast is retrieve in real time, no need to refresh this page.")
        return redirect(reverse('task-result', args=[task.id]))
    except Exception as e:
        messages.add_message(request, messages.WARNING, f"Job cannot be submitted: {e}")
        return redirect(reverse('home')) 


def home(request):
    return render(request, template_name='rmanager/home.html')


def lunchTask(request):
    if request.method == 'POST':
        form = TaskSubmitForm(request.POST)
        if form.is_valid():
            task_data = {
                'trg': form.cleaned_data['trg'],
                'action': form.cleaned_data['action'],
            }
            request.session['task_data'] = task_data
            return redirect(reverse('runner'))
    else:
        form = TaskSubmitForm()
    return render(request, template_name='rmanager/task_lunch.html', context={'form': form})


def taskResult(request, task_id):
    return render(request, template_name='rmanager/task_result.html', context={'taskid': task_id})


@require_http_methods(["GET"])
def getTaskUpdate(request, task_id):
    update = AsyncResult(task_id)
    data = {
        'id': task_id,
        'state': update.state,
        'line': update.info
    }
    return JsonResponse(data)
