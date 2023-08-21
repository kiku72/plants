from django.urls import path
from . import views
from main_app.views import PlantList

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', PlantList.as_view(), name='plants_list'),
    # path('plants/<int:plant_id>/', views.plants_details.as_view(), name='detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
    path('account/signup', views.signup, name='signup'),
]