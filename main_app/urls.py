from django.urls import path
from . import views
from main_app.views import PlantList, PlantExplore
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', PlantList.as_view(), name='plants_list'),
    path('plants/explore', PlantExplore.as_view(), name='plants_explore'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
    path('account/signup', views.signup, name='signup'),
    path('plants/<int:plant_id>/add_photo/', views.add_photo, name='add_photo'),
    path('plants/create_photo/', views.create_photo, name='create_photo'),
    path('plants/<int:plant_id>/add_comment', views.add_comment, name='add_comment'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)