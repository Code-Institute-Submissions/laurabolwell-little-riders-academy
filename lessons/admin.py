from django.contrib import admin
from .models import Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'day',
        'time',
        'min_age',
        'max_age',
        'class_size',
        'duration',
        'price',
        'image'
    )



# Register your models here.
admin.site.register(Lesson, LessonAdmin)
