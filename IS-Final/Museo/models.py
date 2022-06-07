from django.db import models
from django.db.models import Q, CheckConstraint,F

class Artwork(models.Model):
    artwork_name = models.CharField("artwork name", max_length=30, unique=True)
    author = models.CharField("author name", max_length=30)
    valor = models.IntegerField("valor")
    create_date = models.CharField("create date", max_length=50, null= True)
    f_date = models.DateField("f date")
    artistic_movement = models.CharField("artistic movement", max_length=100)
    image = models.ImageField(upload_to='Artwork')
    description = models.TextField()
    
    class Meta: 
        constraints = [CheckConstraint(
        name="valor constraint",
        check=Q(valor__gt=0)),]


    def __str__(self) -> str:
        return self.artwork_name

class PaintStyle(models.Model):
    style = models.CharField("artistic style", max_length=50, primary_key=True)

    def __str__(self) -> str:
        return self.style

class PaintTecnic(models.Model):
    tecnic = models.CharField("artistic tecnic", max_length=50, primary_key=True)

    def __str__(self) -> str:
        return self.tecnic

class Paint(models.Model):
    id = models.OneToOneField(Artwork, verbose_name="pintura", primary_key=True, on_delete=models.CASCADE)
    style = models.ForeignKey(PaintStyle, verbose_name="artistic style", on_delete=models.CASCADE)
    tecnic = models.ForeignKey(PaintTecnic, verbose_name="artistic tecnic", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return Artwork.objects.get(pk=self.id.id).artwork_name

class SculptureStyle(models.Model):
    style = models.CharField("artistic style", max_length=50, primary_key=True)

    def __str__(self) -> str:
        return self.style

class SculptureMaterial(models.Model):
    material = models.CharField("artistic material", max_length=50, primary_key=True)

    def __str__(self) -> str:
        return self.material

class Sculpture(models.Model):
    id = models.OneToOneField(Artwork, verbose_name="sculpture", primary_key=True, on_delete=models.CASCADE)
    style = models.ForeignKey(SculptureStyle, verbose_name="artistic style", on_delete=models.CASCADE)
    material = models.ForeignKey(SculptureMaterial, verbose_name="artistic material", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return Artwork.objects.get(pk=self.id.id).artwork_name

class Room(models.Model):
    room_name = models.CharField("room name", max_length=30, unique=True)

    def __str__(self) -> str:
        return self.room_name

class Expose(models.Model):
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    id_artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    exhibition_start_date = models.DateField("exhibition_start_date")
    exhibition_end_date = models.DateField("exhibition_end_date")
    
    only_one_room_and_artwork = models.UniqueConstraint(
        name="only one room and artwork",
        fields=['id_room', 'id_artwork'],
        deferrable=models.Deferrable.IMMEDIATE
    ) 
    
    class Meta:
        constraints = [ CheckConstraint(
        name="correct date",
        check=Q(exhibition_start_date__lt= F("exhibition_end_date"))
    ), ]

    # correct_date = models.CheckConstraint(
    #     name="correct date",
    #     check=Q(exhibition_start_date__lt=exhibition_end_date)
    # )

    def  __str__(self) -> str:
        return Artwork.objects.get(pk=self.id_artwork.id).artwork_name + " in " + Room.objects.get(pk=self.id_room.id).room_name
