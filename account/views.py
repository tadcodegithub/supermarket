from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter

def loginPage(request):
     context={}
     return render(request,'account/login.html',context)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
        
    context = {'form':form}
    return render(request, 'account/register.html', context)

def logoutUser(request):
     context={}
     return render(request,'account/login.html',context)

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
def Customers(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()
    myFliter = OrderFilter(request.GET, queryset=orders)
    orders = myFliter.qs 
    context = {'customer':customer, 'orders':orders, 
               'order_count':order_count, 'myFliter':myFliter}
    return render(request, 'account/customers.html',context)
def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=3)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'form':formset}
    return render(request, 'account/order_form.html', context)
def updateOrder(request, pk):

	order = Order.objects.filter(id=pk).first()
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'account/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.filter(id=pk).first()
    print("order customer id ",order.customer)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'account/delete.html', context)

