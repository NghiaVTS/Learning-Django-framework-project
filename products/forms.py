from django import forms
import datetime
from phonenumber_field.formfields import PhoneNumberField


class SignUpTable(forms.Form):
    name = forms.CharField(required=True, label="Full name")
    # phoneNumber = PhoneNumberField()
    phoneNumber = forms.CharField(required=True, label="Phone number")
    ammount = forms.IntegerField(required=True, label="Number of people")
    date = forms.DateField(initial=datetime.date.today, required=True)
    time = forms.TimeField(widget=forms.TimeInput(
        format='%H:%M'), required=True)
