from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        exclude = ('user', 'testimonial_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'display_name': 'Anonymous',
            'rating': 'Rating',
            'review': 'Please write your review here'
        }
        labels = {
            'display_name': 'Name (to be displayed with the review)',
            'rating': 'Rating',
            'review': 'Please leave your testimonial here'
        }
        self.fields['display_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'text-navy'
            self.fields[field].widget.attrs['label'] = labels
