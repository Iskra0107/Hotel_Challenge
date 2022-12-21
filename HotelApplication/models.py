from django.db import models
from django.contrib.auth.models import User
from django.db import models
import numpy as np

# Create your models here.

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_address = models.CharField(max_length=50)
    images = models.ImageField(upload_to='images', null=True, blank=True, default='../data/hotel.jpeg')
    desc = models.TextField(null=True, blank=True)
    hotel_geolocation = models.CharField(max_length=10)
    overall_rating = models.CharField(max_length=10, null=True, blank=True)

    def average_rating(self):
        overall_rating = map(lambda x: x.hotel_rating, self.overall_rating.all())
        return np.mean(overall_rating)   #za aritmeticka sredina ili prosek na elementi

    fav = models.ManyToManyField(User, related_name='fav', blank=True)

    def __str__(self):
        return self.hotel_name

    class Meta:
        ordering = ('hotel_name',)


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_review')
    hotel_rating =models.IntegerField(choices=RATING_CHOICES)
    desc_review = models.TextField(null=True, blank=True)
    hotels = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_review')
    likes = models.ManyToManyField(User, related_name='review_likes')

    def like(self):
        return self.likes.count()


class HotelReview(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel_fav = models.ForeignKey(Hotel, on_delete=models.CASCADE)
