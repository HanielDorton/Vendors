from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render_to_response
from django.contrib.auth import authenticate, logout
from furniture.models import *
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from furniture import forms

def get_item_and_vendor_info(request):
	form = forms.skuForm(request.POST)
	try:
		current_item = item.objects.get(sku__iexact=request.POST['request_sku'])
		current_vendor = vendor.objects.get(id=current_item.vendor_id)
		sell = current_item.cost*current_vendor.multy
		if sell > current_item.list:
			sell = current_item.list*.9
		return current_item, current_vendor, sell, form
	except ObjectDoesNotExist:
		pass
	except KeyError:
		pass
	current_item = {'sku':'','desc':'','list':'','cost':''}
	current_vendor = {'name':'','multy':'', 'shipping':''}
	sell = ''
	return current_item, current_vendor, sell, form


def index(request):
	form = forms.taxForm(request.POST)
	try:
		current_city = salestax.objects.get(city__iexact=request.POST['city'])
		current_city.rate *= 100
		current_city.rate = str(current_city.rate)+' %'
	except ObjectDoesNotExist:
		current_city = {'city':'', 'rate':'', 'county':''}
	except KeyError:
		current_city = {'city':'', 'rate':'', 'county':''}
	return render_to_response('index.html', {'salestax':current_city, 'form':form}, context_instance=RequestContext(request))

def customer_view(request):
	current_item, current_vendor, sell, form = get_item_and_vendor_info(request)
	return render_to_response('customer_view.html', {'item':current_item, 'vendor': current_vendor, 'sell':sell, 'form':form}, context_instance=RequestContext(request))
	
def mfc_view(request):
	if not request.user.is_authenticated():
		return redirect('/login/')
	current_item, current_vendor, sell, form = get_item_and_vendor_info(request)
	return render_to_response('MFC_view.html', {'item':current_item, 'vendor': current_vendor, 'sell':sell, 'form':form}, context_instance=RequestContext(request))
	
def logout_view(request):
	logout(request)
	return redirect('/')
	
