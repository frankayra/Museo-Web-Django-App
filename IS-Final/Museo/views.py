from django.shortcuts import render, HttpResponse 
from .CasosDeUso import Catalogo

# Create your views here.

def Home(request):
    return render(request,'home.html') 

def Services(request):
    return render(request,'services.html') 

def RoomCatalog(request):
    rooms = Catalogo.Lista_Salas()
    return render(request, 'room_catalog.html', {'rooms': rooms})

def ArtWorkCatalog(request, room):
    artworks = Catalogo.Obras_por_sala(room)
    return render(request, 'artwork_catalog.html', {'artworks': artworks, 'room': room})

def ArtWorkInfo(request,artworkname,room):
    artwork = Catalogo.Atributos_obra(artworkname)
    return render(request, 'artworkinfo.html', {'artwork': artwork})

