
from django.contrib import admin
from django.urls import path
from .views import list, new, edit, delete
urlpatterns = [
    path('new/', new, name='new'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete<int:pk>', delete, name='delete'),
    path('', list, name='list'),
]
