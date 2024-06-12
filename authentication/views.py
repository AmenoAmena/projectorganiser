from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def login_view(request):
    pass

def register_view(request):
    pass

def logout_view(request):
    logout(request)
    return redirect("login")