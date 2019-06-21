from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from twilio.rest import Client
import random
# Create your views here.



def index(request):
    return render(request, "index.html")




def setings(request):

    a = log.objects.all()

    return render(request, "TABLE.html", {'list': a})


def login123(request):
    logmsg = "Verification on Process"
    if request.method == 'POST':
        Usern = request.POST.get('uname')
        Passw = request.POST.get('psw')
        try:
            abc = log.objects.get(User=Usern, Password=Passw)
            if abc is not None:
                return redirect(index)
        except:
            logmsg= "Login Failed, Please Try Again"
            return render(request,"login.html", {'logmsg': logmsg})

    return render(request, "login.html", {'logmsg': logmsg})




def signup(request):
    form = loginform(request.POST or None)
    if request.method== "POST":
        print("posttttt")
        if form.is_valid():
            form.save()
            a = form.cleaned_data.get('Phone')
            otp = random.randint(00000, 99999)
            request.session['otpp'] = otp
            print(otp)
            account = 'AC0c71b812cffac40e2c1373f4857d2aac'
            token = '673298a5d22de1cf2477b8d92c3f68ab'
            client = Client(account, token)
            client.messages.create(from_='(251) 220-3115', to="+91" + str(a), body='Good day Your verifcation code is ' + str(otp))
            return redirect(otpveri)
    return render(request, "Signup.html", {'form': form})



def testfun(request):
    form = Testform(request.POST)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect(setings)
    return render(request, "testhtml.html", {'form':form})


def delete(request, id):
    abc = log.objects.get(id=id)
    abc.delete()
    return redirect(setings)


def formedi(request, id):
    del_form = get_object_or_404(log, id=id)
    forma = testform(request.POST or None, instance=del_form)
    if request.method == 'POST':
        if forma.is_valid():
            forma.save()
            return redirect('list')
    return render(request, "Signup.html", {'form': forma})

def otpveri(request):

    msg ="otp verification on process"

    if request.method == "POST":

        otp2= request.session['otpp']

        print(otp2 ,"type=", type(otp2))

        orgotp = request.POST.get('otp')

        print(orgotp, "type=", type(orgotp))

        orgg = int(orgotp)
        print(type(orgg))


        if orgg==otp2:
            return render(request, 'index.html')
        else:
            msg = "Sorryyy OTP is not valid"
            return render(request, "otpverification.html", {'msg': msg})

    return render(request, "otpverification.html", {'msg': msg})




