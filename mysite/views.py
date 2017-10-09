from django.shortcuts import render

def index(request):
	return render(request, 'index2.html', {})

def resume(request):
	return render(request, 'resume.html', {})

def education(request):
	return render(request, 'education.html', {})

def work(request):
	return render(request, 'work.html', {})

def contact(request):
	return render(request, 'contact.html', {})

def awards(request):
	return render(request, 'awards.html', {})

def research(request):
	return render(request, 'research.html', {})

def research_current(request):
	return render(request, 'research_current.html', {})

def skills(request):
	return render(request, 'skills.html', {})
