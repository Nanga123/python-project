from django.shortcuts import render, redirect
from .forms import signupform
from qrcode import*
from django.contrib.auth import authenticate,login
import mysql.connector as mysc
import tabulate as t
from django.template import RequestContext
from django.contrib import messages
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
            messages.success(request,("user id or password is incorrect"))
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

def Oppenheimer(request):
    conn=mysc.connect (user='root',host='localhost',passwd='sql123inlife',database='bookmyshow')
    cur=conn.cursor()
    qy='select moviename from movies where moviename="oppenheimer"'
    cur.execute(qy)
    data=cur.fetchall()
    qy2='select cast from movies where moviename="oppenheimer"'
    cur.execute(qy2)
    data1=cur.fetchall()
    qy3='select type from movies where moviename="oppenheimer"'
    cur.execute(qy3)
    data2=cur.fetchall()
    qy4='select language from movies where moviename="oppenheimer"'
    cur.execute(qy4)
    data3=cur.fetchall()
    qy5='select rating from movies where moviename="oppenheimer"'
    cur.execute(qy5)
    data4=cur.fetchall()
    data5={
        'movie_name':(data),
        'movie_cast':(data1),
        'movie_type':(data2),
        'movie_lang':(data3),
        'movie_rate':(data4),

    }

    
    if request.method=="POST" :
        name=request.POST['name']
        phone_no=request.POST['PHONE_NO']
        tickets=request.POST['tickets']
        movie_details=" "
        movie_details+="movie:Oppenheimer,type:thriller,rating:8.6,"
        movie_details+=",username:" + str(name)
        movie_details+=",phone_no:"+ str(phone_no)
        movie_details+=",no_of_tickets:"+ str(tickets)
        img1=make(movie_details)
        img1.save('demo/static/images/test1.png')
    else:

        pass
    return render(request,'oppenheimer.html',data5)
def Jailer(request):
    conn=mysc.connect (user='root',host='localhost',passwd='sql123inlife',database='bookmyshow')
    cur=conn.cursor()
    qy='select moviename from movies where moviename="jailer"'
    cur.execute(qy)
    data=cur.fetchall()
    qy2='select cast from movies where moviename="jailer"'
    cur.execute(qy2)
    data1=cur.fetchall()
    qy3='select type from movies where moviename="jailer"'
    cur.execute(qy3)
    data2=cur.fetchall()
    qy4='select language from movies where moviename="jailer"'
    cur.execute(qy4)
    data3=cur.fetchall()
    qy5='select rating from movies where moviename="jailer"'
    cur.execute(qy5)
    data4=cur.fetchall()
    data5={
        'movie_name':(data),
        'movie_cast':(data1),
        'movie_type':(data2),
        'movie_lang':(data3),
        'movie_rate':(data4),

    }

    
    if request.method=="POST" :
        name=request.POST['name']
        phone_no=request.POST['PHONE_NO']
        tickets=request.POST['tickets']
        movie_details=" "
        movie_details+="movie:jailer,type:action,rating:7.2,"
        movie_details+=",username:" + str(name)
        movie_details+=",phone_no:"+ str(phone_no)
        movie_details+=",no_of_tickets:"+ str(tickets)
        img1=make(movie_details)
        img1.save('demo/static/images/test2.png')
        return render(request,'jailer2.html')
    else:

        pass
    return render(request,'jailer.html',data5)
def Jawan(request):
    conn=mysc.connect (user='root',host='localhost',passwd='sql123inlife',database='bookmyshow')
    cur=conn.cursor()
    qy='select moviename from movies where moviename="jawan"'
    cur.execute(qy)
    data=cur.fetchall()
    qy2='select cast from movies where moviename="jawan"'
    cur.execute(qy2)
    data1=cur.fetchall()
    qy3='select type from movies where moviename="jawan"'
    cur.execute(qy3)
    data2=cur.fetchall()
    qy4='select language from movies where moviename="jawan"'
    cur.execute(qy4)
    data3=cur.fetchall()
    qy5='select rating from movies where moviename="jawan"'
    cur.execute(qy5)
    data4=cur.fetchall()
    data5={
        'movie_name':(data),
        'movie_cast':(data1),
        'movie_type':(data2),
        'movie_lang':(data3),
        'movie_rate':(data4),

    }

    
    if request.method=="POST" :
        name=request.POST['name']
        phone_no=request.POST['PHONE_NO']
        tickets=request.POST['tickets']
        movie_details=" "
        movie_details+="movie:jawan,type:action,rating:7.7,"
        movie_details+=",username:" + str(name)
        movie_details+=",phone_no:"+ str(phone_no)
        movie_details+=",no_of_tickets:"+ str(tickets)
        img1=make(movie_details)
        img1.save('demo/static/images/test3.png')
        return render(request,'jawan2.html')
    else:

        pass
    return render(request,'jawan.html',data5)

def Demonslayer(request):
    conn=mysc.connect (user='root',host='localhost',passwd='sql123inlife',database='bookmyshow')
    cur=conn.cursor()
    qy='select moviename from movies where moviename="Demon slayer:To the swordsmith village"'
    cur.execute(qy)
    data=cur.fetchall()
    qy2='select cast from movies where moviename="Demon slayer:To the swordsmith village"'
    cur.execute(qy2)
    data1=cur.fetchall()
    qy3='select type from movies where moviename="Demon slayer:To the swordsmith village"'
    cur.execute(qy3)
    data2=cur.fetchall()
    qy4='select language from movies where moviename="Demon slayer:To the swordsmith village"'
    cur.execute(qy4)
    data3=cur.fetchall()
    qy5='select rating from movies where moviename=" Demon slayer:To the swordsmith village"'
    cur.execute(qy5)
    data4=cur.fetchall()
    data5={
        'movie_name':(data),
        'movie_cast':(data1),
        'movie_type':(data2),
        'movie_lang':(data3),
        'movie_rate':(data4),

    }

    
    if request.method=="POST" :
        name=request.POST['name']
        phone_no=request.POST['PHONE_NO']
        tickets=request.POST['tickets']
        movie_details=" "
        movie_details+="movie:Demonslayer:Totheswordsmithvillage,type:anime,rating:7.4,"
        movie_details+=",username:" + str(name)
        movie_details+=",phone_no:"+ str(phone_no)
        movie_details+=",no_of_tickets:"+ str(tickets)
        img1=make(movie_details)
        img1.save('demo/static/images/test4.png')
        return render(request,'demonslayer2.html')
    else:

        pass
    return render(request,'demonslayer.html',data5)
def twenty(request):
    conn=mysc.connect (user='root',host='localhost',passwd='sql123inlife',database='bookmyshow')
    cur=conn.cursor()
    qy='select moviename from movies where moviename="2018"'
    cur.execute(qy)
    data=cur.fetchall()
    qy2='select cast from movies where moviename="2018"'
    cur.execute(qy2)
    data1=cur.fetchall()
    qy3='select type from movies where moviename="2018"'
    cur.execute(qy3)
    data2=cur.fetchall()
    qy4='select language from movies where moviename="2018"'
    cur.execute(qy4)
    data3=cur.fetchall()
    qy5='select rating from movies where moviename="2018"'
    cur.execute(qy5)
    data4=cur.fetchall()
    data5={
        'movie_name':(data),
        'movie_cast':(data1),
        'movie_type':(data2),
        'movie_lang':(data3),
        'movie_rate':(data4),

    }

    
    if request.method=="POST" :
        name=request.POST['name']
        phone_no=request.POST['PHONE_NO']
        tickets=request.POST['tickets']
        movie_details=" "
        movie_details+="movie:2018,typesurvival,rating:8.4,"
        movie_details+=",username:" + str(name)
        movie_details+=",phone_no:"+ str(phone_no)
        movie_details+=",no_of_tickets:"+ str(tickets)
        img1=make(movie_details)
        img1.save('demo/static/images/test5.png')
        return render(request,'twenty2.html')
    else:

        pass
    return render(request,'twenty.html',data5)
















































































