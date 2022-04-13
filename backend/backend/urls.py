from django.contrib import admin
from django.urls import path, include
from api import views
from api.views import search_thread

urlpatterns = [
    path('api/v1/', include('api.urls')),
]
