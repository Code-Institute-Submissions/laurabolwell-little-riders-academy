from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'question': 'Question',
            'answer': 'Answer'
        }
        self.fields['question'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'text-navy'
            self.fields[field].label = False
