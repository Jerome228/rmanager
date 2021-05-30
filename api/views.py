# from django.shortcuts import render, HttpResponse
from django.db import models
from django.http import JsonResponse
from rest_framework import generics
from .serializers import AppDataSerializer
from .models import AppData
from .remote_actions import remoteActions
from django_celery_results.models import TaskResult
from django.views.generic import ListView


# Create your views here.
class TaskListView(ListView):
    paginate_by = 15
    model = TaskResult
    template_name = 'api/taskresult_list.html'


class AppDataView(generics.ListAPIView):
    queryset = AppData.objects.all()
    serializer_class = AppDataSerializer


class AppDataCreate(generics.CreateAPIView):
    queryset = AppData.objects.all()
    serializer_class = AppDataSerializer


def remoteCommands(request):
    queryset = AppData.objects.first()
    app = queryset.hservers
    out = remoteActions(app)
    return JsonResponse({'out': out}, content_type='application/json')
