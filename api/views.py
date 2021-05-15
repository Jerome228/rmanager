#from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .serializers import AppDataSerializer
from .models import AppData

# Create your views here.
class AppDataView(generics.ListAPIView):
    queryset = AppData.objects.all()
    serializer_class = AppDataSerializer
