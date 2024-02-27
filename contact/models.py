from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    contact_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    booking_number = models.CharField(max_length=254, null=True, blank=True)
    query = models.TextField(null=False, blank=False)
