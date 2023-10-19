from django.urls import path
from . import views

# Создание перенаправленных url адресов.
urlpatterns = [
    path('', views.start, name='index'),
]