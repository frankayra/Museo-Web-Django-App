from django.contrib import admin
from .models import Room,Expose,Artwork, Sculpture,Paint,PaintStyle,SculptureMaterial,SculptureStyle 
# Register your models here.

admin.site.register(Room)
admin.site.register(Artwork)
admin.site.register(Expose)
admin.site.register(Sculpture)
admin.site.register(SculptureStyle)
admin.site.register(Paint)
admin.site.register(PaintStyle)
admin.site.register(SculptureMaterial) 





