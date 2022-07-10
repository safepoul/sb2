from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def HomeApp(request):
    context={
        
    }
    return render(request,'HomeApp.html',context)