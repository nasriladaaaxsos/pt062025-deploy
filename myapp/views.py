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
    
    