from django.urls import path,include
from . import views

urlpatterns = [
    path('print-hello/',views.print_hello, name="print hello")
]