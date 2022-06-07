# Generated by Django 4.0 on 2022-06-06 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Museo', '0002_remove_expose_id_artwork_remove_expose_id_room_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artwork_name', models.CharField(max_length=30, unique=True, verbose_name='artwork name')),
                ('author', models.CharField(max_length=30, verbose_name='author name')),
                ('valor', models.IntegerField(verbose_name='valor')),
                ('create_date', models.DateField(verbose_name='create date')),
                ('f_date', models.DateField(verbose_name='f date')),
                ('date', models.DateField(verbose_name='date')),
                ('image', models.ImageField(upload_to='Artwork')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=30, unique=True, verbose_name='room name')),
            ],
        ),
        migrations.CreateModel(
            name='Expose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(unique=True, verbose_name='image_url')),
                ('exhibition_start_date', models.DateField(verbose_name='exhibition_start_date')),
                ('exhibition_end_date', models.DateField(verbose_name='exhibition_end_date')),
                ('id_artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Museo.artwork')),
                ('id_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Museo.room')),
            ],
        ),
    ]
