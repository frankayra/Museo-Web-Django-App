# Generated by Django 4.0 on 2022-06-07 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Museo', '0008_paintstyle_painttecnic_sculpturematerial_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expose',
            name='image_url',
        ),
    ]
