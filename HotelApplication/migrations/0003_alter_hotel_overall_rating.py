# Generated by Django 4.1.3 on 2022-11-28 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApplication', '0002_hotel_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='overall_rating',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
