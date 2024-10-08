from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.safestring import mark_safe
import env, json, requests, pandas as pd, os
from datetime import date

class AuthenticationUser:
	def __init__(self,request):
		self.headers = {'Content-Type': 'application/json'}
		self.request = request

	def Login(self):
		values = None
		try:
			payload = json.dumps(self.request.GET)
			response = requests.request("GET", env.LOGIN, headers=self.headers, data=payload)
			values = json.loads(response.text)
			# self.request.session['pk_user'] = values['user']['pk_user']
			# self.request.session['name_user'] = f"{values['user']['first_name']} {values['user']['surname']}"
			# self.request.session['pk_company'] = values['user']['company']
			# self.request.session['data_branch'] = values['data']['data']['all_branch']
			# self.request.session['logo'] = values['data']['data']['fields']['logo']
			# self.request.session['permission'] = values['user']['permission']
			# self.request.session['name_company'] = values['data']['data']['fields']['name']
			# self.request.session['size_permission'] = len(values['user']['permission'])
			# self.request.session['url_application'] = env.URL_APPLICATION
			# self.request.session['url_seller'] = values['url_seller']
			print(env.URL_FILES)
			path_dir = f"{env.URL_FILES}{values['user']['company']}"
			if not os.path.exists(path_dir):
				os.mkdir(path_dir)
		except Exception as e:
			print(e, 'Error')
		return json.dumps({'result': values['result'], 'message': values['message']})


class Employee:
	def __init__(self,request):
		self.headers = {'Content-Type': 'application/json'}
		self.request = request

	def Get_List_Employee_By_Branch(self):
		print(self.request.GET)
		response = requests.request("GET", env.GET_LIST_EMPLOYEE_BY_BRANCH, headers=self.headers, data=json.dumps(self.request.GET))
		return json.dumps(json.loads(response.text))

	def Get_Employee(self,pk_employee):
		response = requests.request("GET", env.GET_EMPLOYEE, headers=self.headers, data=json.dumps({'pk_employee':pk_employee}))
		return json.loads(response.text)

	def Update_User(self, data):
		response = requests.request("PUT", env.UPDATE_USER, headers=self.headers, data=data)
		return json.loads(response.text)


class Setting:
	def __init__(self,request):
		self.headers = {'Content-Type': 'application/json'}
		self.request = request

	def Get_Permission(self):
		response = requests.request("GET", env.GET_PERMISSION, headers={}, data={})
		return json.loads(response.text)

	def Get_Type_Contract(self):
		response = requests.request("GET", env.GET_TYPE_CONTRACT, headers={}, data={})
		return json.loads(response.text)

	def Get_Payroll_Type_Document_Identification(self):
		response = requests.request("GET", env.GET_PAYROLL_TYPE_DOCUMENT_IDENTIFICATION, headers={}, data={})
		return json.loads(response.text)

	def Get_Type_Regimen(self):
		response = requests.request("GET", env.GET_TYPE_REGIMEN, headers={}, data={})
		return json.loads(response.text)

	def Get_Type_Organization(self):
		response = requests.request("GET", env.GET_TYPE_ORGANIZATION, headers={}, data={})
		return json.loads(response.text)

	def Get_Municipalities(self):
		response = requests.request("GET", env.GET_MUNICIPALITIES, headers={}, data={})
		return json.loads(response.text)

	def Get_Type_Worker(self):
		response = requests.request("GET", env.GET_TYPE_WORKER, headers={}, data={})
		return json.loads(response.text)


class Inventory:
	def __init__(self,request):
		self.headers = {'Content-Type': 'application/json'}
		self.request = request

	def Get_List_Products_Company(self):
		payload = json.dumps({
		  "pk_branch": self.request.GET['pk_branch']
		})
		response = requests.request("GET", env.GET_LIST_PRODUCTS_COMPANY, headers=self.headers, data=payload)
		return json.dumps(json.loads(response.text))