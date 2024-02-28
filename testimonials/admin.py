from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'display_name',
        'testimonial_date',
        'rating',
        'review',
    )


admin.site.register(Testimonial, TestimonialAdmin)
