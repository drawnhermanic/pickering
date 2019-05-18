from django import forms
from pickering.models import LogMessage
from pickering.models import Booking

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required

class BookingForm(forms.ModelForm):
    details = forms.CharField( widget=forms.Textarea )
    date_from = forms.DateField(
        input_formats=('%d/%m/%Y', )
        )
    date_to = forms.DateField(
        input_formats=('%d/%m/%Y', )
        )
    class Meta:
        model = Booking
        fields = ("details","date_from","date_to","first_name","last_name","email","phone","visitors",)   # NOTE: the trailing comma is required
