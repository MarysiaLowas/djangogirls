from bootstrap3_datetime.widgets import DateTimePicker
from django import forms

from .models import Job, Meetup


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('company', 'website', 'contact_email', 'title',
                  'description', 'city', 'country')
        # custom labels
        labels = {
            'title': 'Job title'
        }


class MeetupForm(forms.ModelForm):
    meetup_date = forms.DateTimeField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
            "picktime": True}
        )
    )

    class Meta:
        model = Meetup
        fields = ['title', 'organisation', 'meetup_type', 'contact_email',
            'website', 'city', 'country', 'description', 'is_recurring', 
            'recurrence', 'meetup_date'
        ]
