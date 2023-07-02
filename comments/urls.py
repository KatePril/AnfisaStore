from django.urls import path
from .views import *

app_name = 'comments'

urlpatterns = [
    path('comments/', comments, name='comments'),
]
