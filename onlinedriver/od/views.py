from django.shortcuts import render,redirect
from od.models import driverdetail,ownerdetail,ridedetail,counter
# Create your views here.
def index(request):
    request.session['usr']=""
    request.session['usrtype']=""
    request.session['startdate']=""
    request.session['enddate']=""
    request.session['endtime']=""
    request.session['starttime']=""
    return render(request,'index.html')

#o - no ride, 1 - waiting ,2 - in ride


def signup(request):
    if request.method=="POST":
        if request.POST['opt']=='dvr':
            if driverdetail.objects.filter(email=request.POST['your-email']).exists() or request.POST['your-email']=='admin@gmail.com':
                return redirect('od:signup')
            else:
                driverdetail(email=request.POST['your-email'],name=request.POST['full-name'],password=request.POST['password'],experience=request.POST['exp'],dlno=request.POST['dlno'],inride="0",inrideid="0",inridewith="NA",addharno=request.POST['addno'],address=request.POST['address'],pin=request.POST['pincode'],totalrides="0",ratings="0").save()
                return redirect('od:login')
        elif request.POST['opt']=='own':
            if ownerdetail.objects.filter(email=request.POST['your-email']).exists() or request.POST['your-email']=='admin@gmail.com':
                return redirect('od:signup')
            else:
                ownerdetail(email=request.POST['your-email'],name=request.POST['full-name'],password=request.POST['password'],experience=request.POST['exp'],dlno=request.POST['dlno'],inride="0",inrideid="0",inridewith="NA",addharno=request.POST['addno'],address=request.POST['address'],pin=request.POST['pincode']).save()
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
            if driverdetail.objects.filter(email=request.POST['inputEmail'],password=request.POST['inputPassword']).exists():
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


def selectdriver(request):
    if (request.session['usr'] and request.session['usrtype']=='own'):
        a=driverdetail.objects.filter(inride="0")
        return render(request,'selectdriver.html',{'data':a})
    else:
        return redirect('od:login')

def admindash(request):
    if (request.session['usrtype']=='admin' and request.session['usr']=='admin'):
        return render(request,'admin.html')
    else:
        return redirect('od:login')

def dashboard(request):
    print(request.session['usrtype'])
    if (request.session['usr'] and request.session['usrtype']=='usr'):
        a=driverdetail.objects.filter(email=request.session['usr'])
        context={}
        if a[0].inride=="1":
            context['request']=True
            context['inr']=False
            context['data']=ridedetail.objects.filter(rid=a[0].inrideid)[0]
        elif a[0].inride=="2":
            context['inr']=True
            context['request']=False
            context['data']=ridedetail.objects.filter(rid=a[0].inrideid)[0]
        else:
            context['asd']=True
            context['inr']=False
            context['request']=False
        return render(request,'dashboard.html',context)
    else:
        return redirect('od:login')

def ownerdashboard(request):
    if (request.session['usr'] and request.session['usrtype']=='own'):
        a=ownerdetail.objects.filter(email=request.session['usr'])
        context={}
        if a[0].inride=="2":
            context['data']=True
            print("PACCS4")
        else:
            context['data']=False
            print("PACCS5")
        return render(request,'ownerdashboard.html',context)
    else:
        return redirect('od:login')

def createride(request):
    if (request.session['usr'] and request.session['usrtype']=='own'):
        if request.method=="POST":
            request.session['startdate']=request.POST['sd']
            request.session['enddate']=request.POST['ed']
            request.session['endtime']=request.POST['et']
            request.session['starttime']=request.POST['st']
            return redirect('od:selectdriver')
        return render(request,'createride.html')
    else:
        return redirect('od:login')


def confirmride(request,value=None):
    if (request.session['usr'] and request.session['usrtype']=='own'):
        print(value)
        idd=counter.objects.all()

        ownerdetail.objects.filter(email=request.session['usr']).update(inride="1",inrideid=idd[0].rid,inridewith=value)
        driverdetail.objects.filter(email=value).update(inride="1",inrideid=idd[0].rid,inridewith=request.session['usr'])
        ridedetail(driveremail=value,rid=idd[0].rid,owneremail=request.session['usr'],status="Pending",startdate=request.session['startdate'],enddate=request.session['enddate'],starttime=request.session['starttime'],endtime=request.session['endtime']).save()
        counter.objects.filter(rid=idd[0].rid).update(rid=str(int(idd[0].rid)+1))
        return redirect('od:ownerdashboard')
    else:
        return redirect('od:login')


def acceptride(request,value=None):
    print("asdasdasd1")
    if (request.session['usr'] and request.session['usrtype']=='usr'):
        print("asdasdasd22")
        a=ridedetail.objects.filter(rid=value)
        ownerdetail.objects.filter(email=a[0].owneremail).update(inride="2")
        driverdetail.objects.filter(email=a[0].driveremail).update(inride="2")
        ridedetail.objects.filter(rid=value).update(status="InRide")
        print("Suce")
        return redirect('od:dashboard')
    else:
        return redirect('od:login')

def rejectride(request,value=None):
    if (request.session['usr'] and request.session['usrtype']=='usr'):
        a=ridedetail.objects.filter(rid=value)
        ownerdetail.objects.filter(email=a[0].owneremail).update(inride="0",inrideid="0",inridewith="NA")
        driverdetail.objects.filter(email=a[0].driveremail).update(inride="0",inrideid="0",inridewith="NA")
        ridedetail.objects.filter(rid=value).update(status="Cancelled")
        return redirect('od:dashboard')
    else:
        return redirect('od:login')


def finishride(request,value=None):
    if(request.session['usr'] and request.session['usrtype']=='usr'):
        ridedetail.objects.filter(rid=value).update(status="Compleated")
        a=ridedetail.objects.filter(rid=value)
        ownerdetail.objects.filter(email=a[0].owneremail).update(inride="0",inrideid="0",inridewith="NA")
        driverdetail.objects.filter(email=a[0].driveremail).update(inride="0",inrideid="0",inridewith="NA")
        d=driverdetail.objects.filter(email=a[0].driveremail)
        driverdetail.objects.filter(email=a[0].driveremail).update(totalrides=str(int(d[0].totalrides)+1))
        return redirect('od:dashboard')
    else:
        return redirect('od:login')
