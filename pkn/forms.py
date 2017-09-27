from django import forms
from .models import Simulation

class SimForm(forms.ModelForm):
	class Meta:
		model = Simulation
		fields = ('title', 'description',)