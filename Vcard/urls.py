

from django.urls import path
from .views import VcardHome

urlpatterns = [

    path('',VcardHome , name='HomeApp'),
]
