
from django.contrib import admin
from django.urls import path
from .view import *
urlpatterns = [
    path('new/', new, name='new'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete<int:pk>', delete, name='delete'),
    path('', list, name='list'),
]
