from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Student


def index(request):
  data = Student.objects.all()
  context = {"data": data}
  return render(request, "index.html", context)


#def login(request):
  #return render(request, "login.html")

def handlelogin(request):
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    myuser = authenticate(username=username, password=password)

    if myuser is not None:
      login(request, myuser)
      return redirect('/')

    else:
      return redirect('/login')

  return render(request, "registration/login.html")

#def signup(request):
  #return render(request, "signup.html")

def handlesignup(request):
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    # print(username,password)
    myuser = User.objects.create_user(username, password)
    myuser.save()
  return render(request, "signup.html")

def checkout(request):
  return render(request, "checkout.html")

def cart(request):
  return render(request, "cart.html")

def invoice(request):
  return render(request, "invoice.html")
