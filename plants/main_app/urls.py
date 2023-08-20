from django.urls import path
from . import views
from main_app.views import PlantList

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', PlantList.as_view(), name='plants_list'),
]