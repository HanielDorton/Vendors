from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render_to_response
from django.contrib.auth import authenticate, logout
from furniture.models import *
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist

def get_item_and_vendor_info(request):
	if not request.user.is_authenticated():
		return redirect('/login/')
	try:
		current_item = item.objects.get(sku__iexact=request.POST['request_sku'])
		current_vendor = vendor.objects.get(id=current_item.vendor_id)
		sell = current_item.cost*current_vendor.multy
		if sell > current_item.list:
			sell = current_item.list*.9
		return current_item, current_vendor, sell
	except ObjectDoesNotExist:
		pass
	except KeyError:
		pass
	current_item = {'sku':'none','desc':'','list':'','cost':''}
	current_vendor = {'multy':''}
	sell = ''
	return current_item, current_vendor, sell


def index(request):
	if not request.user.is_authenticated():
		return redirect('/login/')
	return render_to_response('index.html')

def customer_view(request):
	current_item, current_vendor, sell = get_item_and_vendor_info(request)
	return render_to_response('customer_view.html', {'item':current_item, 'vendor': current_vendor, 'sell':sell}, context_instance=RequestContext(request))
	
def mfc_view(request):
	current_item, current_vendor, sell = get_item_and_vendor_info(request)
	return render_to_response('MFC_view.html', {'item':current_item, 'vendor': current_vendor, 'sell':sell}, context_instance=RequestContext(request))
	
def logout_view(request):
	logout(request)
	return redirect('/login/')
	
