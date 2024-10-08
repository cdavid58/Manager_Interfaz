from pathlib import Path
import os

_path = os.path.dirname(Path(__file__).resolve()).replace("\\", "/")

# URL_SERVER = "https://evansoft.ddns.net:8585"
URL_SERVER = "http://127.0.0.1:8080"

URL_API_INVOICE = "http://127.0.0.1:9090"

# URL_APPLICATION = "https://evansoft.ddns.net"
URL_APPLICATION = "http://127.0.0.1:8000"


URL_FILES_SERVER = f"{_path}/static/company/"
# URL_FILES_SERVER = "/deploy/static/company/"

URL_FILES_TEMPLATE = f"{_path}/template"
# URL_FILES_TEMPLATE = "/deploy/template"


#URL_UNIVERSAL
#**************************************************************************************************************************************************************************************************************

URL_IN_USE = URL_SERVER
URL_FILES = URL_FILES_SERVER
URL_FILES_TEMPLATE = URL_FILES_TEMPLATE

#**************************************************************************************************************************************************************************************************************

# LOGIN

LOGIN = f"{URL_IN_USE}/user/Login_Company/"


# EMPLOYEE

GET_LIST_EMPLOYEE_BY_BRANCH = f"{URL_API_INVOICE}/user/Get_List_Employee_By_Branch/"
GET_EMPLOYEE = f"{URL_API_INVOICE}/user/Get_Employee/"



# SETTING

GET_PERMISSION = f"{URL_API_INVOICE}/setting/Get_Permission/"
GET_TYPE_CONTRACT = f"{URL_API_INVOICE}/setting/Get_Type_Contract/"
GET_PAYROLL_TYPE_DOCUMENT_IDENTIFICATION = f"{URL_API_INVOICE}/setting/Get_Payroll_Type_Document_Identification/"
GET_TYPE_REGIMEN = f"{URL_API_INVOICE}/setting/Get_Type_Regimen/"
GET_TYPE_ORGANIZATION = f"{URL_API_INVOICE}/setting/Get_Type_Organization/"
GET_MUNICIPALITIES = f"{URL_API_INVOICE}/setting/Get_Municipalities/"
GET_TYPE_WORKER = f"{URL_API_INVOICE}/setting/Get_Type_Worker/"


# EMPLOYEE

UPDATE_USER = f"{URL_API_INVOICE}/user/Update_User/"



# INVENTORY

GET_LIST_PRODUCTS_COMPANY = f"{URL_API_INVOICE}/inventory/Get_List_Products_Company/"

