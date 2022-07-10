from django.shortcuts import render

# Create your views here.
def VcardHome(request):
    context={
        
    }
    return render(request,'VcardHome.html',context)