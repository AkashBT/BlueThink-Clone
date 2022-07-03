from datetime import datetime
from django.db import models
from jsonfield import JSONField
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

################ Employee #####################
class Employee(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    joiningdate=models.DateField(auto_now=True)
    dob=models.DateField()
    phone=models.IntegerField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.fname+' '+self.lname

##################### Login Details ########################
class LoginDetails(models.Model):
    employee=models.CharField(max_length=50)
    date=models.DateField(auto_now=True)
    loginfrom=models.CharField(max_length=50)
    logtime=models.JSONField(blank=True,null=True)
    outtime=models.JSONField(blank=True, null=True,default=list)

    def __str__(self):
        return self.employee


################ Events ##############################
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


############### Project Details ######################
class ProjectDetails(models.Model):
    name=models.CharField(max_length=250)
    cname=models.CharField(max_length=250)
    starttime=models.DateField(blank=True)
    endtime=models.DateField(blank=True)
    assign_to=models.ForeignKey(Employee,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

############## Project Reports #######################
class TodayReport(models.Model):
    pname=models.ForeignKey(ProjectDetails,on_delete=models.CASCADE)
    ename=models.ForeignKey(Employee,on_delete=models.CASCADE)
    tdate=models.CharField(max_length=10)
    workon=RichTextField(blank=True,null=True)



############### FUN IMAGES ############################
class FileUpload(models.Model):
    fileurl=models.TextField(default=None)