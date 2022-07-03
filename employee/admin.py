from django.contrib import admin
from .models import Employee,LoginDetails,ProjectDetails,TodayReport,FileUpload
# Register your models here.

admin.site.register(Employee)
admin.site.register(LoginDetails)
admin.site.register(ProjectDetails)
admin.site.register(TodayReport)
admin.site.register(FileUpload)
