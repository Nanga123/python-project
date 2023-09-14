from django.shortcuts import render, redirect
from .forms import signupform
from qrcode import*
from django.contrib.auth import authenticate,login

from django.template import RequestContext
from django.shortcuts import HttpResponseRedirect

data=None

# Create your views here.

def signupview(request):

    if request.method=='POST':

        form=signupform(request.POST)

        if form.is_valid():

            form.save()
            
            return HttpResponseRedirect('login')
    else:
        form=signupform()

    return render(request,'signup.html',{'form':form})

    return render(request,'signup.html')


def Login(request):

    if request.method=="POST":

        username=request.POST['username']

        password=request.POST['password']


        user= authenticate(username=username,password=password)

        if user is not None:

            login(request,user)
            return HttpResponseRedirect('next')
        else:
            return HttpResponseRedirect('login')
    else:

        return render(request,'login.html')

def homepage(request):

    global data

    if request.method=='POST':

        data=request.POST['data']

        img=make(data)

        img.save('demo/static/images/test.png')
    else:
        pass

    return render(request,'home.html')


def Next(request):

    return render(request,'next.html')

def Trending(request):

    return render(request,'trending.html')

def Home1(request):
    return render(request,'home1.html')





