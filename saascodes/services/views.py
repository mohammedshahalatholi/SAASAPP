from django.shortcuts import render,HttpResponse,redirect
from . forms import servicefrm
from . models import Services
# Create your views here.
def show_services(request):
    data=Services.objects.all()
    return(render(request,'show_services.html',{'data':data}))

def admin_services(request):
    data=Services.objects.all()
    if request.method == 'POST':
        sfrm = servicefrm(request.POST)
        if sfrm.is_valid():
            sfrm.save()
            return redirect('show_services')
    else:
        sfrm = servicefrm()
    return(render(request,'admin_page.html',{'data':data,'sfrm':sfrm}))

def add_services(request):
    if request.method == 'POST':
        sfrm = servicefrm(request.POST)
        if sfrm.is_valid():
            sfrm.save()
            return redirect('show_services')
    else:
        sfrm = servicefrm()
    return render(request, 'add_services.html', {'sfrm': sfrm})


# or use add_services.html

def edit_services(request,pk):
     print('its request',request)
     print('requestpost',request.POST)
     eservises=Services.objects.get(pk=pk)
     print('its eservises',eservises)
     if request.method=='POST':
         efrm=servicefrm(request.POST,instance=eservises)
         print('its e form',efrm)
         if efrm.is_valid():
            efrm.save()
            return(redirect('show_services'))
     else:
         efrm=servicefrm(instance=eservises)
         print('its instanse',eservises)
         print('its e form else',efrm)
     return(render(request,'eservices.html',{'efrm':efrm}))


def delete_services(request,pk):
    dservices=Services.objects.get(pk=pk)
    dservices.delete()
    return(redirect('show_services'))
