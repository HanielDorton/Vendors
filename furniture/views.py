from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render_to_response
from django.contrib.auth import authenticate, logout
from furniture.models import *
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from furniture import forms

def get_item_and_vendor_info(request, vendor_view):
	if vendor_view == '2':
		form = forms.DMIFairplexForm(request.POST)
	elif vendor_view == '3':
		form = forms.CMAmberForm(request.POST)
	elif vendor_view == '4':
		form = forms.BossForm(request.POST)
	elif vendor_view == '5':
		form = forms.FriantGitanaForm(request.POST)
	elif vendor_view == '6':
		form = forms.CMRespondForm(request.POST)
	elif vendor_view == '7':
		form = forms.CMVerdeForm(request.POST)
	elif vendor_view == '8':
		form = forms.CMRubyForm(request.POST)
		elif vendor_view == '9':
		form = forms.CMJadeForm(request.POST)
	else:
		form = forms.USForm(request.POST)
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
		current_city.rate = str(current_city.rate)+' %'
	except ObjectDoesNotExist:
		current_city = {'city':'', 'rate':'', 'county':''}
	except KeyError:
		current_city = {'city':'', 'rate':'', 'county':''}
	return render_to_response('index.html', {'salestax':current_city, 'form':form}, context_instance=RequestContext(request))

def vendors_list(request, view_choice):
	if view_choice == 'MFC_view':
		if not request.user.is_authenticated():
			return redirect('/login/')
	all_vendors = vendor.objects.all().order_by('name')
	return render_to_response('vendor.html', {'all_vendors': all_vendors, 'view_choice': view_choice})
	
def vendor_info(request, view_choice, vendor_choice):
	if not request.user.is_authenticated():
		return redirect('/login/')
	try:
		current_vendor = vendor.objects.get(id=vendor_choice) #.parent_id
		parent_choice = parent_vendor.objects.get(id=current_vendor.parent_id)	
	except ObjectDoesNotExist:
		parent_choice = ""
	except KeyError:
		parent_choice = ""	
	try:
		contacts = contact.objects.filter(parent=parent_choice.id)
	except ObjectDoesNotExist:
		contacts = ""
	except KeyError:
		contacts = ""
	return render_to_response('vendor_info.html', {'contacts':contacts,'parent_choice':parent_choice, 'current_vendor': current_vendor })	
	
def item_search(request, view_choice, vendor_choice):
	if view_choice == "MFC_view":
		if not request.user.is_authenticated():
			return redirect('/login/')
	try:
		vendor_view_name = vendor.objects.get(id=vendor_choice).name
	except ObjectDoesNotExist:
		vendor_view_name = ""
	except KeyError:
		vendor_view_name = ""
	current_item, current_vendor, sell, form = get_item_and_vendor_info(request, vendor_choice)
	return render_to_response('item_search.html', {'view_choice': view_choice, 'vendor_view_name':vendor_view_name, 'item':current_item, 'vendor': current_vendor, 'sell':sell, 'form':form}, context_instance=RequestContext(request))


def logout_view(request):
	logout(request)
	return redirect('/')
	
