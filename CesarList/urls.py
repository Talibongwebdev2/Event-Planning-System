from django.conf.urls import url, include
from django.contrib import admin
from CEList import views 






urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),
    url('admin/', admin.site.urls),    
    url(r'^CEList/cId$', views.custom_view, name='custom_view'),    
    #url(r'^CEList/(\d+)/$', views.events_page, name='events_page'), 
    url('paylist/', views.payroll_list, name='payroll_list'), 
    url('salary/', views.salary_page, name='salary_page'),     
    url(r'^CEList/bId$', views.booking_view, name='booking_view'),
    url('emplist/', views.employee_list, name='employee_list'),
    url('employee/', views.employee_page, name='employee_page'),
    url('emplist/employee/', views.employee_page, name='employee_page'),
    url('report/', views.comp_report, name='comp_report'),
    url('indvrep/', views.comp_report_indv, name='comp_report_indv'),
    url('emprep/', views.emp_report, name='emp_report'),
    url('emprepindv/', views.emp_report_indv, name='emp_report_indv')
   ]
    

