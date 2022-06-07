from django.urls import path, include 
from . import views 
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('home/', views.Home, name = "home"),
    path('services/', views.Services, name = "services"),
    path('catalog/', views.RoomCatalog, name = "catalog"),
    path('catalog/<str:room>/', views.ArtWorkCatalog, name = "artworkcatalog"),
    
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
