from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
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
    # age is not included because it can be calculated using date-planted instead
    fields = ['name', 'date', 'description']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
def signup (request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/plants/')
        else:
            error_message = 'Invalid signup information - try again.'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request,'registration/signup.html', context)