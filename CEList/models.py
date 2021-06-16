from django.db import models

DEPARTMENT_CHOICES = (
    ("Operations" , "operations"),
    ("Quality Assurance" , "QA"),
    ("Human Resource" , "HR"),
    ("Administration" , "Admin"),
    ("Training" , "training")
    )

BRANCH_CHOICES = (
    ("Cavite" , "cavite"),
    ("Manila" , "manila"),
    ("Caloocan" ,"caloocan" ),
    ("Taguig" ,"taguig")
    )

GEN_CHOICES =(
    ("F" , "Female"),
    ("M" , "Male"),
    )


class Employee_info(models.Model):
    Name = models.TextField(default='')
    Age = models.TextField(default='')
    Gender = models.TextField( choices = GEN_CHOICES, default='')
    Address = models.TextField(default='')
    Birthdate = models.DateTimeField(default='')
    Contact_No = models.TextField(default='')
    Emailaddress = models.TextField(default='')
    Company_id = models.TextField(default='')
  
class Employee_Salary(models.Model):
    employee_info = models.ForeignKey(Employee_info, default=None, on_delete=models.CASCADE)
    Days = models.TextField(default='')
    Rate = models.TextField(default='')
    Deduction = models.TextField(default='')
    Status = models.TextField(default='')
    Date_time = models.DateTimeField(default='')
    
class Branch(models.Model): 
    employee_info = models.ManyToManyField(Employee_info, default=None)
    Company_branch = models.CharField(max_length = 20, choices = BRANCH_CHOICES, default ="")
    Company_address = models.TextField(default='')


class Department(models.Model):
    employee_info = models.ManyToManyField(Employee_info, default=None)
    Department = models.CharField(max_length = 20, choices = DEPARTMENT_CHOICES, default ="")
    Dep_status = models.TextField(default='')
    Position = models.TextField(default='')

class Company_report(models.Model):
    employee_info = models.ForeignKey(Employee_Salary, default=None, on_delete=models.CASCADE)
    Companyreport = models.TextField(default='')
    Company_comment = models.TextField(default='')
    Comreport_date = models.DateTimeField(default='')


class Employee_report(models.Model):
    employee_info = models.ForeignKey(Employee_info, default=None, on_delete=models.CASCADE)
    Employeereport = models.TextField(default='')
    Employee_comment = models.TextField(default='')
    Company_rating = models.TextField(default='')
    Empreport_date = models.DateTimeField(default='')

