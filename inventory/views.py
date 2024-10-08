from django.http import HttpResponse
from django.shortcuts import render
from operation import Inventory
import json

def List_Inventory(request):
	return render(request,'inventory/list_inventory.html')


def Get_List_Product_By_Branch(request):
	if request.is_ajax():
		List_Inventory = Inventory(request).Get_List_Products_Company()
		return HttpResponse(List_Inventory)