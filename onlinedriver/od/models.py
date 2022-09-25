from django.db import models

# Create your models here.
class userdetail(models.Model):
    email=models.CharField(max_length=264,unique=True)
    name=models.CharField(max_length=264)
    password=models.CharField(max_length=264)

    def __str__(self):
        return self.email

class ownerdetail(models.Model):
    email=models.CharField(max_length=264,unique=True)
    name=models.CharField(max_length=264)
    password=models.CharField(max_length=264)

    def __str__(self):
        return self.email
