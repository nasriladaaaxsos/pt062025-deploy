from django.shortcuts import render, HttpResponse, redirect
from . import models

# Create your views here.

def index(request):
    context = {
        "hamza" : "test"
    }
    return render(request, "index.html" , context)

def login(request):
    print(f'This is my number' )
    return render(request, "login.html")

def login_form(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        #test 
        print(f" {username }  - {password}")

        if username == "MohammadMfarjeh" and password == "password123":
            request.session['is_logged']  = True  #Store
            #del request.session['is_logged']
            return redirect("/home")  # redirect to home page
        else:
            return redirect('/login')
    else:
        return redirect('/login')

    

def signup(request):
    return render(request, "signup.html")

#Views/Controllers should be skinny, models should be Fat
def reg_form(request):
    if request.method == "POST":
        models.create_user(request.POST)
        request.session['is_logged']  = True
        return redirect('/home')
    else:
        return redirect('/login')
    

def home(request):
    if 'is_logged' in request.session: 
        return render(request, "home.html")
    else:
        return redirect('/login')
    
def sign_out(request):
    del request.session['is_logged']
    return redirect('/login')


def show_all(request):
    context = {
        "allusers" : models.get_all_users()
    }
    return render(request, "show.html" , context )

def viewById(request , id):
    context = {
        "user" : models.get_user_by_id(id)
    }
    return render(request, "details.html" , context)
    

def delete_by_id(request):
    if request.method == "POST":
        if 'is_logged' in request.session: 
            user_id = request.POST['user_id']
            models.delete_user(user_id)
            return redirect('/show')
        else:
            return redirect('/login')
    else:
        return redirect('/login')
    
    
def add_address(request , user_id):
    context = {
        "user_id" : user_id
    }
    return render(request, "addaddress.html" , context)


def add_new_address(request):
    models.add_new_address(request.POST)
    return redirect('/show')


def view_addresses(request, id):
    
    context ={
        "user" : models.get_all_addresss(id)
    }
    return render(request, "viewaddress.html" , context)
    