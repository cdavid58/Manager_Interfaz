from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^List_Employee/$',List_Employee,name="List_Employee"),
	url(r'^Get_List_Employee_By_Branch/$',Get_List_Employee_By_Branch,name="Get_List_Employee_By_Branch"),
	url(r'^Update_User/$',Update_User,name="Update_User"),
	url(r'^Edit/(\d+)/$',Edit,name="Edit"),

]