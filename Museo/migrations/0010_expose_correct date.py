# Generated by Django 4.0 on 2022-06-07 01:11

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('Museo', '0009_remove_expose_image_url'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='expose',
            constraint=models.CheckConstraint(check=models.Q(exhibition_start_date__lt=django.db.models.expressions.F('exhibition_end_date')), name='correct date'),
        ),
    ]
