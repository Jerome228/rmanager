from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.contrib import messages
from .tasks import c_goToSleep


# @require_http_methods(["POST"])
def remoteTask(request):
    result = c_goToSleep.delay(5)
    messages.add_message(request, messages.INFO, "Running commands on remote host...")
    return render(request, template_name='rmanager/home.html')

def home(request):
    return render(request, template_name='rmanager/home.html')
