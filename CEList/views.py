from django.shortcuts import render, redirect
from django.http import HttpResponse
from CEList.models import Employee_info, Employee_Salary, Branch, Company_report, Employee_report
from django.views.decorators.csrf import csrf_exempt


def home_page(request):
    EmployeeInfo = Employee_info.objects.all()
    return render(request, 'homepage.html', {'EmployeeInfo':EmployeeInfo})


def salary_page(request, EmpSalaryId):
    Empsalary = Employee_info.objects.get(id=EmpSalaryId)
    salaries = Employee_Salary.objects.filter(employee_info=EmpSalaryId)
    branch = Branch.objects.get(employee_branch=EmpSalaryId)
    return render(request, 'salary.html', {'employee_info': Empsalary, 'salaries': salaries, 'branch': branch})

def salary_add(request, EmpSalaryId):
    Empsalary = Employee_info.objects.get(id=EmpSalaryId)
    Employee_Salary.objects.create(Rate=request.POST['rate'],Days=request.POST['days'],Deduction=request.POST['deduct'],Total=request.POST['total'],Date_time=request.POST['salarydate'], employee_info=Empsalary)
    return redirect(f'/CEList/empsalary/{Empsalary.id}/')

def payroll_list(request):
    EmployeeInfo = Employee_info.objects.all()
    return render(request, 'Payroll.html', {'employee_info':EmployeeInfo})

def new_employee(request):
    newInfo = Employee_info.objects.create(Name=request.POST['name'],Contact_No=request.POST['contact_num'],Emailaddress=request.POST['email_add'],Age=request.POST['age'],Address=request.POST['address'],Company_id=request.POST['comid'],Gender=request.POST['gender'])
    return redirect(f'/CEList/branch/{newInfo.id}/')     


def employee_page(request):
    return render(request, 'Employeeinfo.html')

def employee_list(request):
    EmployeeInfo = Employee_info.objects.all()
    return render(request, 'emp_list.html', {'employee_info':EmployeeInfo})


def branch_page(request, BranchId):
    EmpBranch = Employee_info.objects.get(id=BranchId)
    #salaries = Employee_Salary.objects.filter(employee_info=EmpSalaryId)
    return render(request, 'BranchSelect.html', {'empbranch': EmpBranch})

def branch_add(request, BranchId):
    EmpBranch = Employee_info.objects.get(id=BranchId)
    Branch.objects.create(Company_branch=request.POST['branch'],Department=request.POST['department'],Position=request.POST['posit'], employee_branch=EmpBranch)
    return redirect('/')



def comp_report(request):
    EmployeeInfo = Employee_info.objects.all()
    return render(request, 'company_report.html', {'employee_info':EmployeeInfo})


def comp_report_indv(request, ComReportId):
    CompanyRep = Employee_info.objects.get(id=ComReportId)
    branch = Branch.objects.get(employee_branch=ComReportId)
    Report = Company_report.objects.filter(employee_comrep=ComReportId)
    return render(request, 'creport_indv.html', {'companyreport':CompanyRep, 'Report': Report, 'branch': branch})

def comp_report_add(request, ComReportId):
    CompanyRep = Employee_info.objects.get(id=ComReportId)
    Company_report.objects.create(Companyreport=request.POST['comreport'],Company_comment=request.POST['comcomment'],Comreport_date=request.POST['creportdate'], employee_comrep=CompanyRep)
   
    return redirect(f'/CEList/comrep/{CompanyRep.id}/')



def emp_report(request):
    EmployeeInfo = Employee_info.objects.all()
    return render(request, 'employee_report.html', {'employee_info':EmployeeInfo})

def emp_report_indv(request, IndvReportId):
    EmployeeRep = Employee_info.objects.get(id=IndvReportId)
    branch = Branch.objects.get(employee_branch=IndvReportId)
    Report = Employee_report.objects.filter(employee_emrep=IndvReportId)
    return render(request, 'empreportindv.html', {'indvreport':EmployeeRep, 'Report': Report, 'branch': branch})

def emp_report_add(request, IndvReportId):
    EmployeeRep = Employee_info.objects.get(id=IndvReportId)
    Employee_report.objects.create(Employeereport=request.POST['Empreport'],Employee_comment=request.POST['Empcomment'],Empreport_date=request.POST['emreport_date'], employee_emrep=EmployeeRep)
   
    return redirect(f'/CEList/indvrepor/{EmployeeRep.id}/')

def emp_personal(request, ID):
    EmployeeInfo = Employee_info.objects.get(id=ID)
    branch = Branch.objects.get(employee_branch=ID)
    return render(request, 'EmpPerInfo.html', {'employee_info':EmployeeInfo, 'branch': branch})



def updateEmployee(request, updateId):
	Employupdate = Employee_info.objects.get(id=updateId)
	branch = Branch.objects.get(employee_branch=updateId)

	#if request.method == "POST":
		#Empupdate = Employee_info.objects.get(id=updateId)
		
		#Employee_info.objects.update(Name=request.POST['name'],Contact_No=request.POST['contact_num'],Emailaddress=request.POST['email_add'],Age=request.POST['age'],Address=request.POST['address'],Company_id=request.POST['comid'],Gender=request.POST['gender'])
	    
		#return redirect('/emplist')

	return render(request, 'Employeeinfo.html', {'employee_info':Employupdate,  'branch': branch})


def updateEmployeeEdit(request, updateId):
	Employupdate = Employee_info.objects.get(id=updateId)

	Employupdate.Name = request.POST['name']	
	Employupdate.Contact_No = request.POST['contact_num']
	Employupdate.Emailaddress = request.POST['email_add']
	Employupdate.Age = request.POST['age']
	Employupdate.Address = request.POST['address']
	Employupdate.Company_id = request.POST['comid']
	Employupdate.Gender = request.POST['gender']
	Employupdate.save()

	return redirect('/emplist')


def deleteEmployee(request, deleteId):
	Empdelete = Employee_info.objects.get(id=deleteId)

	if request.method == "POST":
		Empdelete.delete()
		return redirect('/emplist')
	return render(request, 'emp_delete.html', {'employee_info':Empdelete})





