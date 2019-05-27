from django.db import models

class parameter(models.Model):
	total_number = models.IntegerField(default=0)
	timeout = models.IntegerField(default=0.0)
	skip_probability = models.FloatField(default=0.0)
	arrive_time = models.IntegerField(default=0)
	average_dining_time = models.IntegerField(default=0)
	table_number = models.IntegerField(default=0)
	def __unicode__(self):
		return self.name

class person_information(models.Model):
	name = models.CharField(max_length=20)
	ID_number = models.CharField(max_length=50, blank=True)
	place = models.IntegerField(default=0)
	waiting_time = models.FloatField(default=0.0)
	def __unicode__(self):
		return self.name