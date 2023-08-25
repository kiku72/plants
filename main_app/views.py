import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plant, Photo, Comment
from .forms import CommentForm

# Create your views here.

def home (request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

class PlantList (LoginRequiredMixin, ListView):
    model = Plant

    # Filtering by user
    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user)

class PlantExplore (LoginRequiredMixin, ListView):
    model = Plant

class PlantCreate (LoginRequiredMixin, CreateView):
    model = Plant
    # age is not included because it can be calculated using date-planted instead
    fields = ['name', 'date', 'description']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def plants_detail (request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    comment_form = CommentForm()
    return render(request, 'plants/detail.html', {'plant': plant, 'comment_form': comment_form})

def add_comment(request, plant_id):
    form = CommentForm(request.POST)
    print(plant_id)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user_id = request.user.id
        comment.plant_id = plant_id
        comment.save()
    return redirect('detail', plant_id=plant_id)

class PlantUpdate (LoginRequiredMixin, UpdateView):
    model = Plant
    fields = ['name', 'date', 'description']

class PlantDelete (LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = '/plants'

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

def add_photo (request, plant_id):
    # Photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # Uploaded user photos are named after a unique 6 digit string
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, plant_id=plant_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', plant_id=plant_id)

def create_photo (request, plant_id):
    # Photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # Uploaded user photos are named after a unique 6 digit string
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, plant_id=plant_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)