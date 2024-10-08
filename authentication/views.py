from django.shortcuts import render
from django.http import HttpResponse
from operation import AuthenticationUser

def Login(request):
	if request.is_ajax():
		print(request.GET)
		return HttpResponse(AuthenticationUser(request).Login())
	return render(request,'authentication/login.html')

def Index(request):
	return render(request,'index.html')