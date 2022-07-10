

from django.urls import path
from .views import VcardHome , Vcard_list , Vcard_details , VcardCreate , VcardUpdate


urlpatterns = [

    path('',VcardHome , name='HomeApp'),
    path('APIList' , Vcard_list , name='VcardAPI'),
    path('APIDetails/<pk>' , Vcard_details , name='VcardDetailsAPI'),
    path('APIVcardCreate/' , VcardCreate , name='VcardCreateAPI'),
    path('APIVcardUpdate/<pk>' , VcardUpdate , name='VcardUpdateAPI'),


]
