from django.db import models

class ownerdetail(models.Model):
    email=models.CharField(max_length=264,unique=True)
    name=models.CharField(max_length=264)
    password=models.CharField(max_length=264)
    experience=models.CharField(max_length=264)
    dlno=models.CharField(max_length=264)
    addharno=models.CharField(max_length=264)
    inride=models.CharField(max_length=264)
    address=models.CharField(max_length=264)
    pin=models.CharField(max_length=264)
    inrideid=models.CharField(max_length=264)
    inridewith=models.CharField(max_length=264)
    def __str__(self):
        return self.email

# Create your models here.
class driverdetail(models.Model):
    email=models.CharField(max_length=264,unique=True)
    name=models.CharField(max_length=264)
    password=models.CharField(max_length=264)
    experience=models.CharField(max_length=264)
    dlno=models.CharField(max_length=264)
    inride=models.CharField(max_length=264)
    inrideid=models.CharField(max_length=264)
    inridewith=models.CharField(max_length=264)
    addharno=models.CharField(max_length=264)
    address=models.CharField(max_length=264)
    pin=models.CharField(max_length=264)
    totalrides=models.CharField(max_length=264)
    ratings=models.CharField(max_length=264)
    def __str__(self):
        return self.email

class ridedetail(models.Model):
    rid=models.CharField(max_length=264,unique=True)
    driveremail=models.CharField(max_length=264)
    owneremail=models.CharField(max_length=264)
    startdate=models.CharField(max_length=264)
    enddate=models.CharField(max_length=264)
    starttime=models.CharField(max_length=264)
    endtime=models.CharField(max_length=264)
    status=models.CharField(max_length=264)
    def __str__(self):
        return self.rid

class counter(models.Model):
    rid=models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.rid
