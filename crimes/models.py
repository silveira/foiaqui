from django.db import models

import datetime

class Incident (models.Model):
	"""An localized crime incident"""
	desc = models.TextField()
	lon = models.CharField(maxlength=30)
	lat = models.CharField(maxlength=30)
	when = models.DateField(auto_now_add=True)
	
	def __str__(self):
		"""An string representation of the incident object"""
		return 'INC'+str(self.id)

	def was_today(self):
		"""True if when is current day"""
		return self.when == datetime.date.today()

	# To be visible in the admin interface
	class Admin:
		pass

