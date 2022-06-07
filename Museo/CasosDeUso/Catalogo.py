from Museo.models import Room, Expose, Artwork
from datetime import *



def Obras_por_sala(nombre_sala):
    sala = Room.objects.get(room_name=nombre_sala)
    return sala.expose_set.filter(exhibition_start_date__lte=datetime.now(), exhibition_end_date__gte=datetime.now()).select_related('id_artwork__artwork_name')


    # for tupla in Expose.objects.get(id_room=id_sala):
    #     lista_de_ids_obras.append(tupla.id)

    # for id_obra in lista_ids_obras:
    #     for obra in Artwork.objects.get(id=id_obra):
    #         lista_obras.append(obra.)

def Atributos_obra(nombre_obra):
    return Artwork.objects.get(artwork_name=nombre_obra)



def Lista_Salas():
    return Room.objects.all()