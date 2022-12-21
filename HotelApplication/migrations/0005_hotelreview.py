# Generated by Django 4.1.3 on 2022-11-28 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApplication', '0004_alter_hotel_options_remove_hotel_review_hotel_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotelApplication.hotel')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotelApplication.review')),
            ],
        ),
    ]