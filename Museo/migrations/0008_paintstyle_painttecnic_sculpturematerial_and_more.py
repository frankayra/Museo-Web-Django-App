# Generated by Django 4.0 on 2022-06-07 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Museo', '0007_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaintStyle',
            fields=[
                ('style', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='artistic style')),
            ],
        ),
        migrations.CreateModel(
            name='PaintTecnic',
            fields=[
                ('tecnic', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='artistic tecnic')),
            ],
        ),
        migrations.CreateModel(
            name='SculptureMaterial',
            fields=[
                ('material', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='artistic material')),
            ],
        ),
        migrations.CreateModel(
            name='SculptureStyle',
            fields=[
                ('style', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='artistic style')),
            ],
        ),
        migrations.CreateModel(
            name='Sculpture',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Museo.artwork', verbose_name='sculpture')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Museo.sculpturematerial', verbose_name='artistic material')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Museo.sculpturestyle', verbose_name='artistic style')),
            ],
        ),
        migrations.CreateModel(
            name='Paint',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Museo.artwork', verbose_name='pintura')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Museo.paintstyle', verbose_name='artistic style')),
                ('tecnic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Museo.painttecnic', verbose_name='artistic tecnic')),
            ],
        ),
    ]
