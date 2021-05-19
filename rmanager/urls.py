"""rmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from .views import remoteTask, home, getTaskUpdate, taskResult, lunchTask

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('runner/', remoteTask, name='runner'),
    path('luncher/', lunchTask, name='luncher'),
    path('get-task-update/<str:task_id>/', getTaskUpdate, name='update'),
    path('task/<str:task_id>/', taskResult, name='task-result'),
    path('api/', include('api.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
