from django.conf.urls import url, include
from django.contrib import admin
from CEList import views 






urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),
    url('admin/', admin.site.urls),    
    #url(r'^CEList/cId$', views.custom_view, name='custom_view'),    
    url(r'^CEList/empsalary/(\d+)/$', views.salary_page, name='salary_page'), 
    url(r'^CEList/empsalary/(\d+)/salary_add$', views.salary_add, name='salary_add'), 
    url(r'^CEList/branch/(\d+)/$', views.branch_page, name='branch_page'), 
    url(r'^CEList/branch/(\d+)/branch_add$', views.branch_add, name='branch_add'), 
    url('paylist/', views.payroll_list, name='payroll_list'), 
    url(r'^CEList/new_employee$', views.new_employee, name='new_employee'),
    #url('^CEList/(\d+)/$', views.salary_page, name='salary_page'),     
    #url(r'^CEList/bId$', views.booking_view, name='booking_view'),
    url('emplist/', views.employee_list, name='employee_list'),
    url(r'^CEList/empinfo/(\d+)/$', views.emp_personal, name='emp_personal'),
    url(r'^CEList/empdelete/(\d+)/$', views.deleteEmployee, name='deleteEmployee'),
    url(r'^CEList/empupdate/(\d+)/$', views.updateEmployee, name='updateEmployee'),
    url(r'^CEList/empupdate/(\d+)/update_add$', views.updateEmployeeEdit, name='updateEmployeeEdit'),
    url('employee/', views.employee_page, name='employee_page'),
    url('emplist/employee/', views.employee_page, name='employee_page'),
    url('report/', views.comp_report, name='comp_report'),
    url('indvrep/', views.comp_report_indv, name='comp_report_indv'),
    url(r'^CEList/comrep/(\d+)/$', views.comp_report_indv, name='comp_report_indv'), 
    url(r'^CEList/comrep/(\d+)/comrep_add$', views.comp_report_add, name='comp_report_add'), 
    url('emprep/', views.emp_report, name='emp_report'),
    url(r'^CEList/indvrepor/(\d+)/$', views.emp_report_indv, name='emp_report_indv'),
    url(r'^CEList/indvrepor/(\d+)/emprep_add$', views.emp_report_add, name='emp_report_add')
   ]
    

