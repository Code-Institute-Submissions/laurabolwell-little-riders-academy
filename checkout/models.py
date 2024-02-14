import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings

from lessons.models import Lesson


class Booking(models.Model):
    booking_number = models.CharField(
        max_length=32, null=False,
        editable=False
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = models.CharField(max_length=40, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    booking_total = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=False, default=0
    )

    def _generate_booking_number(self):
        """
        Generate a random, unique booking number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update booking total each time a booking item is added
        """
        self.booking_total = self.bookingitems.aggregate(
            Sum('bookingitem_total'))['bookingitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the booking number
        if it hasn't already been set
        """
        if not self.booking_number:
            self.booking_number = self._generate_booking_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.booking_number


class BookingItem(models.Model):
    booking = models.ForeignKey(
        Booking, null=False, blank=False,
        on_delete=models.CASCADE, related_name='bookingitems'
    )
    lesson = models.ForeignKey(
        Lesson, null=False, blank=False,
        on_delete=models.CASCADE
    )
    date = models.DateField(null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    bookingitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set bookingitem_total
        and update the booking total
        """
        self.bookingitem_total = self.lesson.price * self.quantity
        super().save(*args, **kwargs)

        def __str__(self):
            return f'{self.lesson.name} on booking {self.booking_number}'
