from django.contrib import admin
from .models import Booking, BookingItem


class BookingItemAdminInline(admin.TabularInline):
    model = BookingItem
    readonly_fields = ('bookingitem_total',)


class BookingAdmin(admin.ModelAdmin):
    inlines = (BookingItemAdminInline,)
    readonly_fields = (
        'booking_number', 'date', 'booking_total',
        'original_basket', 'stripe_pid'
    )

    fields = (
        'booking_number', 'user_profile', 'full_name', 'email',
        'phone_number', 'street_address1', 'street_address2',
        'town_or_city', 'postcode', 'country',
        'date', 'booking_total', 'original_basket', 'stripe_pid'
    )

    list_display = (
        'booking_number', 'full_name', 'phone_number',
        'date', 'booking_total'
    )

    ordering = ('-date',)


admin.site.register(Booking, BookingAdmin)
