from django.db import models
from django.utils import timezone


class Simulation(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	description = models.TextField()
	published_date = models.DateTimeField(
		default=timezone.now)
	created_date = models.DateTimeField(
		default=timezone.now)
	completed_date = models.DateTimeField(
		blank=True, null=True)

	def complete(self):
		self.completed_date = timezone.now()
		self.save()

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

