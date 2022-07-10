from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vcard
from .serializars import VcardSerializer


# Create your views here.
def VcardHome(request):
    context={
        
    }
    return render(request,'VcardHome.html',context)


@api_view(["GET"])
def Vcard_list(request):
    Vcards = Vcard.objects.all()
    Vcards_serilizers = VcardSerializer(Vcards , many=True)
    return Response(Vcards_serilizers.data)


@api_view(["GET"])
def Vcard_details(request , pk):
    Vcard = Vcard.objects.get(id=pk)
    Vcard_serilizers = VcardSerializer(Vcard , many=False)
    return Response(Vcard_serilizers)

@api_view(["POST"])
def VcardCreate(request):
    Vcard = VcardSerializer(data=request.data)

    if Vcard.is_valid():
        Vcard.save()

    return Response(Vcard.data)


@api_view(["POST"])
def VcardUpdate(request , pk):
    instance = Vcard.objects.get(id=pk)
    Vcard_serializaer = VcardSerializer( instance=instance ,  data=request.data)

    if Vcard_serializaer.is_valid():
        Vcard_serializaer.save()

    return Response(Vcard.data)