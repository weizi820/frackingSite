from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Simulation 
from .forms import SimForm

def main_page(request):
	return render(request, 'pkn/pkn_main.html', {})

def sim_list(request):
	sims = Simulation.objects.filter(published_date__lte=timezone.now()).order_by('completed_date')
	return render(request, 'pkn/sim_list.html', {'simulations': sims})

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
	return redirect('post_detail', pk=pk)
	
@login_required
def sim_remove(request, pk):
	sim = get_object_or_404(Simulation, pk=pk)
	sim.delete()
	return redirect('sim_list')