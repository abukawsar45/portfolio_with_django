from django.urls import path
from base.views import *

app_name = 'base'
urlpatterns = [
    path('', index, name='base'),
]