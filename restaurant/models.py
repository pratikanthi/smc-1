from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Restaurant(models.Model):
	full_name=models.CharField(max_length=200, null=False, primary_key=True)
	full_address=models.CharField(max_length=255, null=False)
	contact=models.IntegerField(null=False )
	website=models.CharField(max_length=200, blank=True, null=True)
	name_slug = models.SlugField()
	opening_hours = models.CharField(max_length=50, blank=True, null=True)
	additional_info = models.CharField(max_length=200, blank=True, null=True)
	parking = models.BooleanField(default = False)
	history = models.TextField(null=True)
	
	def __unicode__(self):
		return self.full_name
	