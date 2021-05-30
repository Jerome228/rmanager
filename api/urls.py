from django.urls import path
from .views import AppDataView, AppDataCreate, remoteCommands, TaskListView

app_name = 'api'
urlpatterns = [
    path('', AppDataView.as_view(), name='home'),
    path('new/', AppDataCreate.as_view(), name='new'),
    path('run/', remoteCommands, name='run'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
]
