from django.shortcuts import render,HttpResponse,redirect
from . forms import servicefrm
from . models import Services
# Create your views here.
def show_services(request):
    data=Services.objects.all()
    return(render(request,'static/show_services.html',{'data':data}))

def admin_services(request):
    data=Services.objects.all()
    return(render(request,'static/admin_page.html',{'data':data}))

def add_services(request):
    if request.method =='POST':
        sfrm=servicefrm(request.POST)
        print(sfrm)
        if sfrm.is_valid():
            sfrm.save()
            return(redirect('show_services'))
    else:
        sfrm=servicefrm()
    return(render(request,'static/add_services.html',{'sfrm':sfrm}))

def edit_services(request,pk):
     eservises=Services.objects.get(pk=pk)
     if request.method=='POST':
         efrm=servicefrm(request.POST,instance=eservises)
         if efrm.is_valid():
            efrm.save()
            return(redirect('show_services'))
     else:
         efrm=servicefrm(instance=eservises)
     return(render(request,'static/eservices.html',{'efrm':efrm}))


def delete_services(request,pk):
    dservices=Services.objects.get(pk=pk)
    dservices.delete()
    return(redirect('show_services'))
