from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plant

# Create your views here.

def home (request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

class PlantList (ListView):
    model = Plant

class PlantCreate (CreateView):
    model = Plant
    # age is not included because it can be calculated with date-planted instead
    fields = ['name', 'date', 'description']

class PlantDetailView (DetailView):
    model = Plant

class PlantUpdate (UpdateView):
    model = Plant
    fields = ['name', 'date', 'description']

class PlantDelete (DeleteView):
    model = Plant
    success_url = '/plants'