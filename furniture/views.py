from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render, redirect, render_to_response
from django.contrib.auth import authenticate, logout
from furniture.models import *
from django.template import RequestContext

def index(request):
	if not request.user.is_authenticated():
		return redirect('/login/')
	'''
	if request.method == 'POST':
		current_item = get_object_or_404(item, sku__iexact=request.POST['request_sku'])
	else:
		current_item = get_object_or_404(item, sku__iexact="700637")
	'''
	current_item = item.objects.filter(sku__iexact=request.POST['request_sku']) or item.objects.filter(sku__iexact="700637")
	current_vendor = get_object_or_404(vendor, id=current_item.vendor_id)
	return render_to_response('index.html', {'item':current_item, 'vendor': current_vendor}, context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return redirect('/login/')
	
