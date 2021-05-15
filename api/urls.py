from django.urls import path
from .views import AppDataView

urlpatterns = [
    path('', AppDataView.as_view()),
]