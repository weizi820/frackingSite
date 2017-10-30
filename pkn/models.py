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

class DesignSimulation(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	save_date = models.DateTimeField(
		blank=True,null=True)

	def store(self):
		self.save_date = timezone.now()
		self.save()

	list_of_units = (
		('Pa', 'Pa/m/s'),
		('MPa', 'MPa/mm/s'),
		)
	unit = models.CharField(#label="Units", 
		choices=list_of_units,
		max_length=200,
		default='Pa/m/s')
	length = models.FloatField(#label="Fracture length", 
		default=1000)
	height = models.FloatField(#label="Fracture height",
		default=51.8)
	q = models.FloatField(#label="Fluid injection flow rate",
		default=0.0662)
	young_mod = models.FloatField(#label="Young's modulus",
		default=5.5783e10)
	nu = models.FloatField(#label="Poisson's ratio", 
		default=0.3)
	mu = models.FloatField(#label="Fluid viscosity",
		default=0.2)
	fluid_loss_coeff = models.FloatField(#label="Fluid loss coefficient",
		default=9.84e-6)
	spurt_coeff = models.FloatField(#label="Spurt loss coefficient",
		default=0)

	list_of_balance_models = (
			('noleak', 'No leak-off'),
			('carter', 'Carter leak-off'), 
			('largeleak', 'Large leak-off'),)
	balance = models.CharField(#label="Material balance model", 
		choices=list_of_balance_models,
		max_length=200,
		default='No leak-off')
	# TODO: set default values to example from book and cite

class AnalysisSimulation(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	created_date = models.DateTimeField(
		default=timezone.now)

	list_of_units = (
		('Pa', 'Pa/m/s'),
		('MPa', 'MPa/mm/s'),
		)
	unit = models.CharField(#label="Units", 
		choices=list_of_units,
		max_length=200)
	start_time = models.FloatField(#label="Simulation start time", 
		default=0)
	end_time = models.FloatField(#label="Simulation end time",
		default=12000)
	inc = models.FloatField(#label="Time increment",
		default=1)
	height = models.FloatField(#label="Fracture height",
		default=51.8)
	q = models.FloatField(#label="Fluid injection flow rate",
		default=0.0662)
	young_mod = models.FloatField(#label="Young's modulus",
		default=5.5783e10)
	nu = models.FloatField(#label="Poisson's ratio", 
		default=0.3)
	mu = models.FloatField(#label="Fluid viscosity",
		default=0.2)
	fluid_loss_coeff = models.FloatField(#label="Fluid loss coefficient",
		default=9.84e-6)
	spurt_coeff = models.FloatField(#label="Spurt loss coefficient",
		default=0)
	list_of_balance_models = (
			('noleak', 'No leak-off'),
			('carter', 'Carter leak-off'), 
			('largeleak', 'Large leak-off'),)
	balance = models.CharField(#label="Material balance model", 
		choices=list_of_balance_models,
		max_length=200)
	# TODO: set default values to example from book and cite

