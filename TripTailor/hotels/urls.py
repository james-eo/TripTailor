from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hotels-home'),
    path('about/', views.about, name='hotels-about'),
    path('accommodations/', views.accommodations, name='accommodations'),
    #path('search/', views.search_results, name='search_results'),
    #path('hotel/<int:hotel_id>/', views.hotel_details, name='hotel_details'),
]
    
