from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def Home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }
    return render(request,"account/dashboard.html", context)
def Products(request):
    products = Product.objects.all()
    return render(request,"account/products.html", {'products':products})
def Customers(request):
    return render(request,"account/customers.html")
