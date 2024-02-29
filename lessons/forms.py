from django import forms
from .widgets import CustomClearableFileInput
from .models import Lesson


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = '__all__'

    image = forms.ImageField(
        widget=CustomClearableFileInput, label='Image', required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'text-navy'
