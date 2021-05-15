from django.urls import path
from .views import AppDataView, AppDataCreate, remoteCommands

app_name = 'api'
urlpatterns = [
    path('', AppDataView.as_view(), name='home'),
    path('new/', AppDataCreate.as_view(), name='new'),
    path('run/', remoteCommands, name='run'),
]
