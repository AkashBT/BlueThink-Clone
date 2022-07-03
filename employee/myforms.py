from .models import Employee,ProjectDetails,TodayReport
from django import forms
from django.contrib.auth.hashers import check_password

class Employee_Register(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    retype_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Employee
        fields = ['fname','lname','email','dob','phone']

    def clean(self):
        super().clean()
        p=self.cleaned_data.get('password')
        p1=self.cleaned_data.get('retype_password')
        if p!=p1 or len(p)<6:
            raise forms.ValidationError("Error password : Both Password did not match...")

class Profile(forms.ModelForm):
    class Meta:
        model=Employee
        fields = ['fname','lname','email','dob','phone']    

class Employeelogin(forms.Form):
    email=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        e=self.cleaned_data.get("email")
        p=self.cleaned_data.get("password")
        try:
            sel=Employee.objects.get(email=e)
        except:
            raise forms.ValidationError("User Does Not Exits")
        else:
            if not check_password(p,sel.password):
                raise forms.ValidationError("Password does not match")


class DateInput(forms.DateInput):
    input_type = 'date'


class Project(forms.ModelForm):
    class Meta:
        model=ProjectDetails
        fields = ['name','cname','starttime','endtime','assign_to'] 
        widgets = {
            'name':forms.TextInput({ "placeholder": "Enter Project Name"}),
            'cname':forms.TextInput({ "placeholder": "Enter Company Name"}),
            'starttime': DateInput(),
            'endtime': DateInput(),
        } 


class TodayReportForm(forms.ModelForm):
    class Meta:
        model=TodayReport
        fields = ['pname','tdate','workon']
        widgets = {
            'tdate': DateInput(),
        } 