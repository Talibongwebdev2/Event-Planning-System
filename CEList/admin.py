from django.contrib import admin
from .models import Employee_info, Employee_Salary, Branch, Employee_report, Company_report


admin.site.register(Employee_info)
admin.site.register(Employee_Salary)
admin.site.register(Branch)
admin.site.register(Company_report)
admin.site.register(Employee_report)
