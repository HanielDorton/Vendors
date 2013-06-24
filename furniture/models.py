from django.db import models
from django.core import urlresolvers

class vendor(models.Model):

	name = models.CharField(max_length=25)
	multy = models.FloatField(default=0)
	shipping = models.CharField(max_length=100)

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

class salestax(models.Model):

	city = models.CharField(max_length=50)
	rate = models.FloatField(default=0)
	county = models.CharField(max_length=50)

	def __unicode__(self):
		return self.city
	
	def get_absolute_url(self):
		return urlresolvers.reverse('non_admin:widget_update', args=(self.pk,))
