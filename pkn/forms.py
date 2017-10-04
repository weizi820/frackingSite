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
	length = forms.FloatField(label="Fracture length")
	height = forms.FloatField(label="Fracture height")
	q = forms.FloatField(label="Fluid injection flow rate")
	young_mod = forms.FloatField(label="Young's modulus")
	nu = forms.FloatField(label="Poisson's ratio", min_value=0.01, max_value = 0.99)
	mu = forms.FloatField(label="Fluid viscosity")
	fluid_loss_coeff = forms.FloatField(label="Fluid loss coefficient")
	spurt_coeff = forms.FloatField(label="Spurt loss coefficient")
	list_of_balance_models = (
			('no-leak', 'No leak-off'),
			('carter', 'Carter leak-off'), 
			('large-leak', 'Large leak-off'),)
	balance = forms.ChoiceField(label="Material balance model", choices=list_of_balance_models)

class AnalysisForm(forms.Form):
	start_time = forms.FloatField(label="Simulation start time")
	end_time = forms.FloatField(label="Simulation end time")
	inc = forms.FloatField(label="Time increment")
	height = forms.FloatField(label="Fracture height")
	q = forms.FloatField(label="Fluid injection flow rate")
	young_mod = forms.FloatField(label="Young's modulus")
	nu = forms.FloatField(label="Poisson's ratio", min_value=0.01, max_value = 0.99)
	mu = forms.FloatField(label="Fluid viscosity")
	fluid_loss_coeff = forms.FloatField(label="Fluid loss coefficient")
	spurt_coeff = forms.FloatField(label="Spurt loss coefficient")
	list_of_balance_models = (
			('no-leak', 'No leak-off'),
			('carter', 'Carter leak-off'), 
			('large-leak', 'Large leak-off'),)
	balance = forms.ChoiceField(label="Material balance model", choices=list_of_balance_models)
	# TODO: set default values and min/max values