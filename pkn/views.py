from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .pkn import pkn_plot_design, pkn_plot_analysis
from .models import Simulation, DesignSimulation, AnalysisSimulation
from .forms import SimForm, SignUpForm, DesignForm, AnalysisForm, AnalysisFormSave

def pkn_main(request):
	return render(request, 'pkn/pkn_main.html', {})

def pkn_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('pkn_main')
    else:
        form = SignUpForm()
    return render(request, 'pkn/pkn_signup.html', {'form': form})

def pkn_design(request):
	if request.method == 'POST':
		form = DesignForm(request.POST)
		if form.is_valid():
			# L = form.cleaned_data['length']
			# h = form.cleaned_data['height']
			# q = form.cleaned_data['q']
			# E = form.cleaned_data['young_mod']
			# nu = form.cleaned_data['nu']
			# mu = form.cleaned_data['mu']
			# C = form.cleaned_data['fluid_loss_coeff']
			# Sp = form.cleaned_data['spurt_coeff']
			# balance = form.cleaned_data['balance']
			design_sim = form.save(commit=False)
			design_sim.author = request.user
			design_sim.save()
			# (t, ww0, pnw) = pkn_plot_design(L, h, q, E, nu, mu, C, Sp, balance)
			(t, ww0, pnw) = pkn_plot_design(design_sim)
			
			design_sim.t = t
			design_sim.ww0 = ww0
			design_sim.pnw = pnw
			# design_sim.length = 
			# request.session['t'] = t
			# request.session['ww0'] = ww0
			# request.session['pnw'] = pnw
			# request.session['length'] = L

			return redirect('pkn_design_results', pk=design_sim.pk)
	else:
		form = DesignForm()
	return render(request, 'pkn/pkn_design.html', {'form': form})

def pkn_analysis(request):
	if request.method == 'POST':
		form = AnalysisForm(request.POST)
		if form.is_valid():
			tstart = form.cleaned_data['start_time']
			tend = form.cleaned_data['end_time']
			inc = form.cleaned_data['inc']
			h = form.cleaned_data['height']
			q = form.cleaned_data['q']
			E = form.cleaned_data['young_mod']
			nu = form.cleaned_data['nu']
			mu = form.cleaned_data['mu']
			C = form.cleaned_data['fluid_loss_coeff']
			Sp = form.cleaned_data['spurt_coeff']
			balance = form.cleaned_data['balance']
			pkn_plot_analysis(tstart, tend, inc, h, q, E, nu, mu, 
								C, Sp, balance)
			
			return redirect('pkn_analysis_results')
	else:
		form = AnalysisForm()
	return render(request, 'pkn/pkn_analysis.html', {'form': form})

def pkn_design_results(request, pk):
	design_sim = get_object_or_404(DesignSimulation, pk=pk)
	# t = request.session['t']
	# ww0 = request.session['ww0']
	# pnw = request.session['pnw']
	# L = request.session['length']
	return render(request, 'pkn/pkn_design_results.html', {'design_sim': design_sim})

def pkn_analysis_results(request):
	return render(request, 'pkn/pkn_analysis_results.html', {})

def pkn_help(request):
	return render(request, 'pkn/pkn_help.html', {})

def pkn_error(request):
	return render(request, 'pkn/pkn_error.html', {})
	
@login_required
def sim_list(request):
	sims = Simulation.objects.filter(author=request.user).order_by('completed_date')
	design_sims = DesignSimulation.objects.filter(author=request.user).order_by('save_date')
	return render(request, 'pkn/sim_list.html', {'simulations': design_sims})

def sim_detail(request, pk):
	sim = get_object_or_404(Simulation, pk=pk)
	return render(request, 'pkn/sim_detail.html', {'sim': sim})

@login_required
def sim_new(request):
	if request.method == "POST":
		form = SimForm(request.POST)
		if form.is_valid():
			sim = form.save(commit=False)
			sim.author = request.user
			sim.save()
			return redirect('sim_detail', pk=sim.pk)
	else:
		form = SimForm()
	return render(request, 'pkn/sim_edit.html', {'form': form})

@login_required
def sim_edit(request, pk):
    sim = get_object_or_404(Simulation, pk=pk)
    if request.method == "POST":
        form = SimForm(request.POST, instance=sim)
        if form.is_valid():
            sim = form.save(commit=False)
            sim.author = request.user
            sim.save()
            return redirect('sim_detail', pk=sim.pk)
    else:
        form = SimForm(instance=sim)
    return render(request, 'pkn/sim_edit.html', {'form': form})

@login_required
def sim_draft_list(request):
    sims = Simulation.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'pkn/sim_draft_list.html', {'sims': sims})

@login_required
def sim_publish(request, pk):
	sim = get_object_or_404(Simulation, pk=pk)
	sim.publish()
	return redirect('sim_detail', pk=pk)
	
@login_required
def sim_remove(request, pk):
	sim = get_object_or_404(Simulation, pk=pk)
	sim.delete()
	return redirect('sim_list')

@login_required
def design_sim_remove(request, pk):
	design_sim = get_object_or_404(DesignSimulation, pk=pk)
	design_sim.delete()
	return redirect('pkn_main')

def design_sim_save(request, pk):
	design_sim = get_object_or_404(DesignSimulation, pk=pk)
	design_sim.store()
	return redirect('sim_list')