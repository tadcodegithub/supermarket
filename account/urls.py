from django.urls import path

from . import views
urlpatterns = [
    path("",views.Home, name='home'),
    path("products/",views.Products, name="products"),
    path('customers/<str:pk_test>/', views.Customers, name="customers"),
    path('order_form/',views.createOrder, name="order_form"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]
