from django.urls import path     
from . import views

#http://localhost:8000/login

urlpatterns = [
    path('', views.index),        #landing page 
    path('login/', views.login, name = "login_route"),
    path('reg/' , views.signup),
    path('regFrom/' , views.reg_form),
    path("login_form" , views.login_form),
    path("home" , views.home),
    path("signout", views.sign_out),
    path("show", views.show_all),
    path("viewById/<int:id>" , views.viewById),
    path("delete_by_id" , views.delete_by_id),
    path("addaddress/<int:user_id>" , views.add_address),
    path("addnewaddress", views.add_new_address),
    path("viewaddress/<int:id>", views.view_addresses)
]