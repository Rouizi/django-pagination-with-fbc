# app/urls.py
from django.contrib import admin
from django.urls import path

from core.views import list_users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_users/<int:page>/', list_users, name='list_users')
]