from django.urls import path, include, re_path 
from . import views 

urlpatterns = [
    path('home/', views.Home, name = "home"),
    path('services/', views.Services, name = "services"),
    path('catalog/', views.RoomCatalog, name = "catalog"),
    path('catalog/<str:room>/', views.ArtWorkCatalog, name = "artworkcatalog"),
    path('catalog/<str:room>/<str:artworkname>/', views.ArtWorkInfo, name = "artworkinfo"),

    
]


