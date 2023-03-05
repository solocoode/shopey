from django.shortcuts import render

def index(request):
  return render(request, "index.html")

def login(request):
  return render(request, "login.html")

def signup(request):
  return render(request, "signup.html")

def checkout(request):
  return render(request, "checkout.html")

def cart(request):
  return render(request, "cart.html")

def invoice(request):
  return render(request, "invoice.html")