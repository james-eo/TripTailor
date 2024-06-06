from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hotels-home'),
    path('about/', views.about, name='hotels-about'),
    path('accommodations/', views.accommodations, name='accommodations'),
    path('get_regions/<int:country_id>/', views.get_regions, name='get_regions'),
    path('get_cities/<int:region_id>/', views.get_cities, name='get_cities'),
    
]
    
