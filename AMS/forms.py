from django import forms
from .models import formBook

class BookingForm(forms.ModelForm):
    class Meta:
        model = formBook
        fields = ['firstname', 'lastname', 's_id', 'room', 'time_in', 'time_out']
        