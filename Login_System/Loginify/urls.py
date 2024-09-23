from django.urls import path,include
from . import views

urlpatterns=[
    path('print-hello/',views.print_hello, name= "print hello"),
    path('get-all-data/',views.get_all_data,name = "get-all-data")
]


    
    

