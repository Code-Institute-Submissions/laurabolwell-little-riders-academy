from django.db import models
from django.contrib.auth.models import User


class Testimonial(models.Model):
    RATING_CHOICES = (
        ('1', '1',),
        ('2', '2',),
        ('3', '3',),
        ('4', '4',),
        ('5', '5',),
    )

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    display_name = models.CharField(
        max_length=254, null=False, blank=False, default='Anonymous'
    )
    testimonial_date = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(
        max_length=5, choices=RATING_CHOICES,
        default='5', null=False, blank=False
    )
    review = models.TextField(null=False, blank=False)
