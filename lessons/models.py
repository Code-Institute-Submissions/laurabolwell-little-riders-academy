from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

DAY_CHOICES = (
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),
)

TIME_CHOICES = (
    ("9:00am", "9:00am"),
    ("10:00am", "10:00am"),
    ("11:00am", "11:00am"),
    ("12:00pm", "12:00pm"),
    ("1:00pm", "1:00pm"),
    ("2:00pm", "2:00pm"),
    ("3:00pm", "3:00pm"),
)


class Lesson(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    min_age = models.PositiveIntegerField(
        default=2,
        validators=[MinValueValidator(2), MaxValueValidator(10)],
        null=False, blank=False
    )
    max_age = models.PositiveIntegerField(
        default=10,
        validators=[MinValueValidator(2), MaxValueValidator(10)],
        null=False, blank=False
    )
    class_size = models.PositiveIntegerField(
        default=12,
        validators=[MinValueValidator(4), MaxValueValidator(15)],
        null=False, blank=False
    )
    duration = models.PositiveIntegerField(
        default=45, null=False, blank=False
    )
    price = models.DecimalField(
        max_digits=4, decimal_places=2,
        default=4.75, null=False, blank=False
    )
    day = models.CharField(
        max_length=15, choices=DAY_CHOICES,
        default="Saturday", null=False, blank=False
    )
    time = models.CharField(
        max_length=15, choices=TIME_CHOICES,
        default="12:00pm", null=False, blank=False
    )
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name
