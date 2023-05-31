"""
URL configuration for tools project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import logging
import datetime

from django.contrib import admin
from django.urls import path
from expo.views import nodes, home, validators

logger = logging.getLogger('django')

def log_request(request):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = request.META.get('REMOTE_ADDR')
    logger.info('Date: %s | Path: %s | Method: %s | IP: %s' % (now, request.path, request.method, ip))
    return None

urlpatterns = [
    path('', home, name='home'),
    path('validators/', validators, name='validators'),
    path('nodes/', nodes, name='nodes'),
]

urlpatterns.append(path('', log_request))
