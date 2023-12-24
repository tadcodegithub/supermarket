from django.urls import path

from . import views
urlpatterns = [
    path("",views.Home),
    path("products/",views.Products),
    path("customers/",views.Customers),
]
