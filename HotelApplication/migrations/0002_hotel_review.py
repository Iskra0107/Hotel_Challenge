# Generated by Django 4.1.3 on 2022-11-28 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApplication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='review',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HotelApplication.review'),
            preserve_default=False,
        ),
    ]
