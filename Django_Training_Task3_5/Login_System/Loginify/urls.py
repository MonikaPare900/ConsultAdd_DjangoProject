from django.urls import path,include
from Loginify import views

urlpatterns = [
    path('print-h/',views.print_hello, name="print-hello" ),
    path('get-all-userdata/',views.get_all_userdata, name="get-all-userdata"),
    path('get-single-user/',views.single_user_data, name="get-single-user"),
    path('signup',views.signup_page,name = 'signup'),
    path('Login',views.login_page,name = 'Login'),
    path('Success',views.confirmation_page,name = 'Success'),
    

]
               