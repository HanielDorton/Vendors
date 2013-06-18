from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from furniture.models import *

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/success/')
        else:
            return redirect('/failedlogin/')
    else:
        return redirect('/failedlogin/')
		
def logout(request):
	return redirect('/login/')

def index(request, request_sku):
	if not request.user.is_authenticated():
		return redirect('/login/')
	item = get_object_or_404(item, name__iexact=request_sku)
	return redirect('/login/')
		
def failedlogin(request):
	return redirect('/login/')
	
def success(request):
	return redirect('/login/')
