from django.http import HttpResponse
from django.shortcuts import render
from operation import Employee, Setting
import json

def List_Employee(request):
	return render(request,'employee/list_employee.html')

def Get_List_Employee_By_Branch(request):
	if request.is_ajax():
		return HttpResponse(Employee(request).Get_List_Employee_By_Branch())

def Edit(request,pk_employee):
	employee = Employee(request).Get_Employee(pk_employee)
	s = Setting(request)
	request.session['pk_employee'] = pk_employee
	return render(request,'employee/edit.html',{'employee':employee, 
		'permission':s.Get_Permission(),
		'Get_Type_Contract':s.Get_Type_Contract(),
		'Get_Payroll_Type_Document_Identification':s.Get_Payroll_Type_Document_Identification(),
		'Get_Type_Regimen':s.Get_Type_Regimen(),
		'Get_Type_Organization':s.Get_Type_Organization(),
		'Get_Municipalities':s.Get_Municipalities(),
		'Get_Type_Worker':s.Get_Type_Worker(),
	})

def Update_User(request):
	if request.is_ajax():
		json_data = list(request.GET.keys())[0]
		data = json.loads(json_data)
		data['pk_employee'] = request.session['pk_employee']
		return HttpResponse(json.dumps(Employee(request).Update_User(json.dumps(data))))