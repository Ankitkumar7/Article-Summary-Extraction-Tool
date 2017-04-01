from __future__ import unicode_literals

from django.db import models

# Create your models here.

class URL(models.Model):
	url = models.CharField(max_length=1000)
	def __unicode__(self):
		return self.url
