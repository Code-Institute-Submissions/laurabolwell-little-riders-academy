from django.db import models

DAY_CHOICES = (
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),
)


class Lessons(models.Model):
    name = models.CharField(max_length=254),
    description = models.TextField(),
    min_age = models.SmallIntegerField(),
    max_age = models.SmallIntegerField(),
    class_size = models.SmallIntegerField(),
    price = models.DecimalField(),
    day = models.CharField(max_length=15, choices=DAY_CHOICES, default="Saturday")
    time = models.TimeField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
