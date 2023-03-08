from django.urls import path
from onepiece.views import *

app_name='oda'

urlpatterns = [
    path('ennies_lobby/',ennies_lobby,name='soccer'),
    path('wano/',wano,name='ego')
]
