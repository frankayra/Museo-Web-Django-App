# Generated by Django 4.0 on 2022-06-06 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Museo', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expose',
            name='id_artwork',
        ),
        migrations.RemoveField(
            model_name='expose',
            name='id_room',
        ),
        migrations.DeleteModel(
            name='Artwork',
        ),
        migrations.DeleteModel(
            name='Expose',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
