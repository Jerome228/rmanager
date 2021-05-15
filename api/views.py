# from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework import generics
from .serializers import AppDataSerializer
from .models import AppData
from .remote_actions import remoteActions


# Create your views here.
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