from datetime import date
from django.conf import settings
from django import forms
from datetimewidget.widgets import DateTimeWidget
from django.contrib.admin.widgets import AdminDateWidget
from .models import Appointment,Technician


class AppointmentForm(forms.ModelForm):

    booking_date = forms.DateField(help_text="YYYY-MM-DD",widget=AdminDateWidget) 
    
    class Meta:

        model = Appointment
        
        fields = ('technician', 'booking_date', 'timeslot')
    
        

    def clean_date(self):
        day = self.cleaned_data['booking_date']

        if day <= date.today():
            raise forms.ValidationError('Date should be upcoming (tomorrow or later)', code='invalid')
        if day.isoweekday() in (0, 6):
            raise forms.ValidationError('Date should be a workday', code='invalid')

        return day