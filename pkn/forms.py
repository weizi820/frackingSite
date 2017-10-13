from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Simulation

class SimForm(forms.ModelForm):
	class Meta:
		model = Simulation
		fields = ('title', 'description',)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class DesignForm(forms.Form):
	list_of_units = (
		('Pa', 'Pa/m/s'),
		('MPa', 'MPa/mm/s'),
		)
	unit = forms.ChoiceField(label="Units", choices=list_of_units)
	length = forms.FloatField(label="Fracture length", initial=1000)
	height = forms.FloatField(label="Fracture height",initial=51.8)
	q = forms.FloatField(label="Fluid injection flow rate",initial=0.0662)
	young_mod = forms.FloatField(label="Young's modulus",initial=5.5783e10)
	nu = forms.FloatField(label="Poisson's ratio", min_value=0.01, max_value = 0.99,initial=0.3)
	mu = forms.FloatField(label="Fluid viscosity",initial=0.2)
	fluid_loss_coeff = forms.FloatField(label="Fluid loss coefficient",initial=9.84e-6)
	spurt_coeff = forms.FloatField(label="Spurt loss coefficient",initial=0)
	list_of_balance_models = (
			('noleak', 'No leak-off'),
			('carter', 'Carter leak-off'), 
			('largeleak', 'Large leak-off'),)
	balance = forms.ChoiceField(label="Material balance model", choices=list_of_balance_models)
	# TODO: set default values to example from book and cite

class AnalysisForm(forms.Form):
	list_of_units = (
		('Pa', 'Pa/m/s'),
		('MPa', 'MPa/mm/s'),
		)
	unit = forms.ChoiceField(label="Units", choices=list_of_units)
	start_time = forms.FloatField(label="Simulation start time", initial=0)
	end_time = forms.FloatField(label="Simulation end time",initial=12000)
	inc = forms.FloatField(label="Time increment",initial=1)
	height = forms.FloatField(label="Fracture height",initial=51.8)
	q = forms.FloatField(label="Fluid injection flow rate",initial=0.0662)
	young_mod = forms.FloatField(label="Young's modulus",initial=5.5783e10)
	nu = forms.FloatField(label="Poisson's ratio", min_value=0.01, max_value = 0.99,initial=0.3)
	mu = forms.FloatField(label="Fluid viscosity",initial=0.2)
	fluid_loss_coeff = forms.FloatField(label="Fluid loss coefficient",initial=9.84e-6)
	spurt_coeff = forms.FloatField(label="Spurt loss coefficient",initial=0)
	list_of_balance_models = (
			('noleak', 'No leak-off'),
			('carter', 'Carter leak-off'), 
			('largeleak', 'Large leak-off'),)
	balance = forms.ChoiceField(label="Material balance model", choices=list_of_balance_models)
	# TODO: set default values to example from book and cite
