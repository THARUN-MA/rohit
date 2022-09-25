from django.shortcuts import render,redirect
from od.models import userdetail,ownerdetail
# Create your views here.
def index(request):
    request.session['usr']=""
    request.session['usrtype']=""
    return render(request,'index.html')

def signup(request):
    if request.method=="POST":
        if request.POST['opt']=='dvr':
            if userdetail.objects.filter(email=request.POST['your-email']).exists() or request.POST['your-email']=='admin@gmail.com':
                return redirect('od:signup')
            else:
                userdetail(email=request.POST['your-email'],name=request.POST['full-name'],password=request.POST['password']).save()
                return redirect('od:login')
        elif request.POST['opt']=='own':
            if ownerdetail.objects.filter(email=request.POST['your-email']).exists() or request.POST['your-email']=='admin@gmail.com':
                return redirect('od:signup')
            else:
                ownerdetail(email=request.POST['your-email'],name=request.POST['full-name'],password=request.POST['password']).save()
                return redirect('od:login')
    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        if request.POST['ch']=='admin':
            if (request.POST['inputEmail']=='admin@gmail.com' and request.POST['inputPassword']=='@1geniUs'):
                request.session['usrtype']='admin'
                request.session['usr']='admin'
                return redirect('od:admindash')
        elif request.POST['ch']=='usr':
            if userdetail.objects.filter(email=request.POST['inputEmail'],password=request.POST['inputPassword']).exists():
                    request.session['usr']=request.POST['inputEmail']
                    request.session['usrtype']='usr'
                    return redirect('od:dashboard')
        elif request.POST['ch']=='cns':
            if ownerdetail.objects.filter(email=request.POST['inputEmail'],password=request.POST['inputPassword']).exists():
                    request.session['usr']=request.POST['inputEmail']
                    request.session['usrtype']='own'
                    return redirect('od:ownerdashboard')
        else:
            print('NO')
            return redirect('od:login')
    return render(request,'login.html')



def logout(request):
    request.session['usr']=""
    request.session['usrtype']=""
    return render(request,'index.html')

def dashboard(request):
    if (request.session['usr'] and request.session['usrtype']=='usr'):
        return render(request,'dashboard.html')
    else:
        return redirect('od:login')

def ownerdashboard(request):
    if (request.session['usr'] and request.session['usrtype']=='own'):
        return render(request,'ownerdashboard.html')
    else:
        return redirect('od:login')

def admindash(request):
    if (request.session['usrtype']=='admin' and request.session['usr']=='admin'):
        return render(request,'admin.html')
    else:
        return redirect('od:login')
