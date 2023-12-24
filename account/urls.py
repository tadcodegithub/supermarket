from django.urls import path

from . import views
urlpatterns = [
    path("",views.Home, name='Home'),
    path("products/",views.Products, name="products"),
    path('customers/<str:pk_test>/', views.Customers, name="customers"),
]
