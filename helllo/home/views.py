from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def gallery(request):
    return render(request, 'gallery.html')  

def team(request):
    return render(request, 'team.html')

def keepintouch(request):
    return render(request, 'keepintouch.html')



def contact(request):
    if request.method =="POST":
        
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
       
        

        contact=Contact(   email= email, name=name,  phone= phone, desc=desc, date= datetime.today())
        
        contact.save()
        messages.success(request, 'Your form has been sent!!......')
    return render(request, 'contact.html')


