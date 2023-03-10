# Generated by Django 4.1.3 on 2022-11-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApplication', '0003_alter_hotel_overall_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotel',
            options={'ordering': ('hotel_name',)},
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='review',
        ),
        migrations.AddField(
            model_name='hotel',
            name='review',
            field=models.ManyToManyField(to='HotelApplication.review'),
        ),
    ]
