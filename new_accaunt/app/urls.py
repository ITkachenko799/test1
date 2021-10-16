from django.urls import path
from .views import *

urlpatterns = [
    path('', task1),
    path('task2',task2)
    ]