from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^List_Inventory/$',List_Inventory,name="List_Inventory"),
	url(r'^Get_List_Product_By_Branch/$',Get_List_Product_By_Branch,name="Get_List_Product_By_Branch"),

]