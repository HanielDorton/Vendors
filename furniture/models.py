from django.db import models
from django.core import urlresolvers

class parent_vendor(models.Model):
	name = models.CharField(max_length=25)
	website = models.URLField()
	address = models.TextField()
	
	def __unicode__(self):
		return self.name

class vendor(models.Model):
	name = models.CharField(max_length=25)
	discount = models.FloatField(default=0)
	multy = models.FloatField(default=0)
	shipping = models.CharField(max_length=100)
	parent = models.ForeignKey(parent_vendor, default=1)

	def __unicode__(self):
		return self.name

class item(models.Model):

	sku = models.CharField(max_length=50)
	desc = models.CharField(max_length=50)
	list = models.FloatField(default=0)
	cost = models.FloatField(default=0)
	vendor = models.ForeignKey(vendor)

	def __unicode__(self):
		return self.sku
		
class catalogue(models.Model):
	name = models.CharField(max_length=40)
	url = models.URLField()
	vendor = models.ForeignKey(vendor)
	
	def __unicode__(self):
		return self.name
	
class contact(models.Model):
	name = models.CharField(max_length=40)
	title = models.CharField(max_length=20, default="Rep")
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	parent = models.ForeignKey(parent_vendor)
	
	def __unicode__(self):
		return self.name

class salestax(models.Model):

	city = models.CharField(max_length=50)
	rate = models.FloatField(default=0)
	county = models.CharField(max_length=50)

	def __unicode__(self):
		return self.city
	
	def get_absolute_url(self):
		return urlresolvers.reverse('non_admin:widget_update', args=(self.pk,))