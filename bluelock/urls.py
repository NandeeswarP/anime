from django.urls import path
from bluelock.views import *

app_name='sai'

urlpatterns = [
    path('soccer/',soccer,name='soccer'),
    path('ego/',ego,name='ego')
]
