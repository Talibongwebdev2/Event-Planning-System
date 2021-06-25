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
    Name = models.CharField(max_length=30)
    Age = models.CharField(max_length=3)
    Address = models.CharField(max_length=50)
    Contact_No = models.CharField(max_length=20)
    Emailaddress = models.CharField(max_length=30)
    Company_id = models.CharField(max_length=10)
    Gender = models.CharField(max_length=10, choices = GEN_CHOICES)
    
    def __str__(self):
        return self.Name
  
class Employee_Salary(models.Model):
    employee_info = models.ForeignKey(Employee_info, default=None, on_delete=models.CASCADE)
    Days = models.TextField(default='')
    Rate = models.TextField(default='')
    Deduction = models.TextField(default='')
    Total = models.TextField(default='')
    Date_time = models.DateTimeField(default='')

    def __str__(self):
        return self.Date_time
    
class Branch(models.Model): 
    employee_branch = models.OneToOneField(Employee_info, default=None, on_delete=models.CASCADE)
    Company_branch = models.CharField(max_length = 20, choices = BRANCH_CHOICES, default ="")
    Department = models.CharField(max_length = 20, choices = DEPARTMENT_CHOICES, default ="")
    Position = models.TextField(default='')

    def __str__(self):
        return self.Company_branch

class Company_report(models.Model):
    employee_comrep = models.ForeignKey(Employee_info, default=None, on_delete=models.CASCADE)
    Companyreport = models.TextField(default='')
    Company_comment = models.TextField(default='')
    Comreport_date = models.DateTimeField(default='')

    def __str__(self):
        return str(self.Comreport_date)


class Employee_report(models.Model):
    employee_emrep = models.ForeignKey(Employee_info, default=None, on_delete=models.CASCADE)
    Employeereport = models.TextField(default='')
    Employee_comment = models.TextField(default='')
    Empreport_date = models.DateTimeField(default='')

    def __str__(self):
        return str(self.Empreport_date)

