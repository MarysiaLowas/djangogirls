from datetimewidget.widgets import DateTimeWidget
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
        widget=DateTimeWidget(
            attrs={'id':"yourdatetimeid"},
            usel10n = True,
            bootstrap_version=3
        )
    )

    class Meta:
        model = Meetup
        fields = ['title', 'organisation', 'meetup_type', 'contact_email',
            'website', 'city', 'country', 'description', 'is_recurring', 
            'recurrence', 'meetup_date'
        ]
