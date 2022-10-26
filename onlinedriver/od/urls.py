from django.conf.urls import url,include
from od import views

app_name='od'

urlpatterns=[
    url('login/',views.login,name='login'),
    url('signup/',views.signup,name='signup'),
    url('logout/',views.logout,name='logout'),
    url('acceptride/(?P<value>\w+)$',views.acceptride,name='acceptride'),
    url('dashboard/',views.dashboard,name='dashboard'),
    url('admindash/',views.admindash,name='admindash'),
    url('rejectride/(?P<value>\w+)$',views.rejectride,name='rejectride'),
    url('finishride/(?P<value>\w+)$',views.finishride,name='finishride'),
    url('ownerdash/',views.ownerdashboard,name='ownerdashboard'),
    url('createride/',views.createride,name='createride'),
    url('selectdriver/',views.selectdriver,name='selectdriver'),
    url('confirmride/(?P<value>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',views.confirmride,name='confirmride'),

]
