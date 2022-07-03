from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='employee'

urlpatterns = [
    
    path('',views.index,name="index"),
    path('register/',views.EmployeeSignup,name="register"),
    path('logout/<int:pk>',views.logout,name="logout"),


    path('dashboard/',views.dashboard,name="dashboard"),
    path('dashboard/profile/<int:pk>',views.profile,name="profile"),


    path('attendance/',views.attendance,name="attendance",),


    path('assign_project/',views.projectdetail,name="projectdetail"),
    path('create_project_report/',views.create_project_report,name="create_project_report"),


    path('image_section/',views.image_upload,name="image_upload"),


    path('generate_salary_slip/',views.generate_salary_slip,name="generate_salary_slip"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)