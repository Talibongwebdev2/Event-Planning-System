from django import forms
from django.forms import ModelForm
from .models import Employee_info, Employee_Salary


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee_info
        fields = '__all__'

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Employee_Salary
        fields = '__all__'

