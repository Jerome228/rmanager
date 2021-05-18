from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from celery.result import AsyncResult
from .tasks import c_runCommands


# @require_http_methods(["POST"])
def remoteTask(request):
    task = c_runCommands.delay()
    messages.add_message(request, messages.INFO, "Job submitted.")
    return render(request, template_name='rmanager/home.html', context={'task': task,})

def home(request):
    return render(request, template_name='rmanager/home.html')

def getTaskUpdate(request, t_id):
    update = AsyncResult(t_id)
    data = {
        'id': t_id,
        'state': update.state,
        'line': update.info
    }
    return JsonResponse(data)
