from xmlrpc.client import DateTime
from django import views
from django.shortcuts import render,redirect,HttpResponseRedirect
from .myforms import Employee_Register,Employeelogin,Profile,Project,TodayReportForm
from .models import Employee,LoginDetails,ProjectDetails,TodayReport,FileUpload
from django.contrib.auth.hashers import make_password
from datetime import datetime, date
import calendar
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import date
from .models import *
from .utils import Calendar
import calendar 
from calendar import HTMLCalendar, month
from django.core.files.storage import FileSystemStorage
from .models import FileUpload
from django.contrib import messages
# Create your views here.




############# LOGIN #############################################
def index(request):
    f=Employeelogin(request.POST or None)
    if f.is_valid():
        e = f.cleaned_data.get("email")
        obj = Employee.objects.get(email=e)
        request.session['user_log']={'id':obj.id,'fname':obj.fname,'lname':obj.lname,'email':obj.email}
        
        try:
            user_data=LoginDetails.objects.get(employee=e)
            
            for key ,value_list in user_data.logtime[-1].items():
                if key == str(date.today()):
                    value_list.append(str(datetime.now().time()))
                    user_data.save()
                else:
                    user=LoginDetails.objects.get(employee=e)
                    dict_for_datetime={}
                    list_for_time=[]
                    date_today=str(date.today())
                    time_now= str(datetime.now().time())
                    list_for_time.append(time_now)
                    dict_for_datetime[date_today]=list_for_time
                    user_data.logtime.append(dict_for_datetime)
                    user_data.save()
                
        except:
            l=LoginDetails()
            l.employee=e
            l.logtime=list()
            l.save()
            user=LoginDetails.objects.get(employee=e)
            dict_for_datetime={}
            list_for_time=[]
            date_today=str(date.today())
            time_now= str(datetime.now().time())
            list_for_time.append(time_now)
            dict_for_datetime[date_today]=list_for_time
            user.logtime.append(dict_for_datetime)
            user.save()

        return redirect("employee:dashboard")
    return render(request,'employee/index.html',{'form':f})    



########### REGISTER ############################################
def EmployeeSignup(request):
    if not request.session['userlog']:
        f=Employee_Register(request.POST or None)
        if f.is_valid():
            sel=f.save(commit=False)    
            p=f.cleaned_data.get('password')
            encp = make_password(p)
            sel.password=encp
            sel.save()
            return redirect("employee:index")
        return render(request,'employee/register.html',{'form':f})
    else:
        return redirect('/dashboard/')



######################### LOGOUT #########################################
def logout(request,pk):
    
    user=LoginDetails.objects.get(employee=request.session['user_log']['email'])
    
    if not user.outtime:
        list_for_time=[]
        dict_for_all_data={}
        date_today=str(date.today())
        time_now= str(datetime.now().time())
        list_for_time.append(time_now)
        dict_for_all_data[date_today]=list_for_time
        user.outtime.append(dict_for_all_data)
        user.save()
    else:
       
        for key ,value_list in  user.outtime[-1].items():
            if str(key) == str(date.today()):
                value_list.append(str(datetime.now().time()))
                user.save()
            else:
                user=LoginDetails.objects.get(employee=request.session['user_log']['email'])
                dict_for_datetime={}
                list_for_time=[]
                date_today=str(date.today())
                time_now= str(datetime.now().time())
                list_for_time.append(time_now)
                dict_for_datetime[date_today]=list_for_time
                user.outtime.append(dict_for_datetime)
                user.save()
               
    request.session.pop("user_log")
    return redirect("employee:index") 

########################### DASHBOARD ##########################################
def dashboard(request):
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    cal=HTMLCalendar().formatmonth(currentYear,currentMonth,currentDay) 
    data=LoginDetails.objects.get(employee=request.session["user_log"]['email'])
    print(data,'===================================')
    for i in data.logtime :
        if str(date.today()) in i:
            login_date=date.today()
            login_time=i[str(date.today())]
    fixed_time="11:00:00:00"
    return render(request,'employee/dashboard.html',{'calender':cal,'login_date':login_date,'login_time':login_time})


###################### PROFILE ########################################
def profile(request,pk):
    if request.method=="GET":
        emp=Employee.objects.get(pk=pk)
        f=Profile(instance=emp)
        return render(request,'employee/profile.html',{'form':f})
    else:
        f=Profile(request.POST)
        print(f,'-----------------------------------------------------')
        if f.is_valid():
            f.save()
        return redirect("employee:dashboard")

 
    
############################### ATTENDANCE ##########################################
def attendance(request):
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    cal=HTMLCalendar().formatmonth(currentYear,currentMonth,currentDay) 
    email=request.session['user_log']['email']
    print(email)
    data=LoginDetails.objects.get(employee=email)
    print(data,'===================================')
    for i in data.logtime :
        if str(date.today()) in i:
            login_date=date.today()
            login_time=i[str(date.today())]
    final_logindata=data.logtime  
    final_logoutdata=data.outtime
    fixed_time="11:00:00:00"
    newdate=date.today()
    tdm=str(date.today().strftime("%Y-%m"))
    # print(type(final_data))
    return render(request,'employee/attendance.html',{'cal':cal,'tdm':tdm,'fixed_time':fixed_time,'final_data':final_logindata,'final_logoutdata':final_logoutdata,'login_date':login_date,'login_time':login_time})


############################ PROJECT ASSIGN ##########################################
def projectdetail(request):
    if request.method=="GET":
        f=Project()
        return render(request,'employee/projectassign.html',{'form':f})
    else:
        f=Project(request.POST)
        print(f,'-----------------------------------------------------')
        if f.is_valid():
            f.save()
        return redirect("employee:dashboard")

########################## PROJECT REPORT ##############################################
def create_project_report(request):
    if request.method=="GET":
        f=TodayReportForm()
        return render(request,'employee/create_project_report.html',{'form':f})
    else:
        f=TodayReportForm(request.POST)
        print(f,'-----------------------------------------------------')
        if f.is_valid():
            f.save()
        return redirect("employee:dashboard")

#################### SHOW FUN IMAGE ##################################################

def image_upload(request):
    if request.method=="POST":
        # request_file = request.FILES['document'] if 'document' in request.FILES else None
        files = request.FILES.getlist('document')
        
        # print(files)
        
        a=[]
        if files:
            for file in files:
                fs = FileSystemStorage()
                filename = fs.save(file.name, file)
                file_url = fs.url(filename)
                a.append(file_url)
            
            fileurl=FileUpload(fileurl=a)
            messages.success(request,'images uploaded successfully.....')
            fileurl.save()
        
        return HttpResponseRedirect('/')
    else:
        images=FileUpload.objects.all()
        datadict={}
        for i in images:
            newid=i.id

            newfile=((i.fileurl).lstrip('[')).rstrip(']')
            a=((newfile.replace("'","")).replace(" ","")).split(",")

            for j in a:

                    datadict[j[7:]]=newid
            if images == None:
                print("see0000000000000000000")
            
            print(datadict)
        return render(request,'employee/fun_images.html',{'images':images,'data':datadict})



################ Generate SALARY SLIP #############################
def generate_salary_slip(request,pk):
    month=pk
    print(orders,'--------------------------------')
    # return render(request,'store/invoice.html',{'order':orders,'customer':customer})
    rendered = render_to_string('employee/generate_salary_slip.html', {'order':orders,'customer':customer})
    return HttpResponse(rendered)

