from django import forms
from .models import Schedule


class ScheduleCreateForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ('category', 'subject', 'title', 'detail', 'deadline')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.help_text
