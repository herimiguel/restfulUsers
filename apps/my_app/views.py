from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import User

# Create your views here.
def index(request):
    context= { 
        'users':User.objects.all()
    }
    return render(request, 'my_app/index.html', context)

def adding(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        email= request.POST['email']
        User.objects.create(first_name=first_name, last_name=last_name, email=email)

    return redirect('/')

def addUserPage(request):
    return render(request,'my_app/addUserPage.html')

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/')

def editUser(request, id):
    context={
        'user':User.objects.get(id=id)
    }
    return render(request, 'my_app/editUser.html', context)

def showUser(request, id):
    context={
        'user':User.objects.get(id=id)
    }
    return render(request, 'my_app/displayUser.html', context)

def updateUser(request, id):
    user= User.objects.get(id=id)
    user.first_name= request.POST['first_name']
    user.last_name= request.POST['last_name']
    user.email= request.POST['email']
    user.save()
    return redirect('/')
     
    
    


 